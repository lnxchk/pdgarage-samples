"""A Random Python Pulumi program"""

import pulumi
import pulumi_pagerduty as pagerduty

user_ids = ["PUSER1", "PUSER2", "PUSER3"]
demo_team_id = "PTEAMID"
deps_count = 0
dependencies = {}

def create_demo_service(srv_name):
    service = pagerduty.Service(srv_name["name"], escalation_policy = demo_ep.id)
    srv_name["id"] = service.id


def create_tech_dep(dependent_service, supporting_service):
    # throw away. 
    global deps_count, dependencies
    dep_str = f"dep{deps_count}"
    dep = pagerduty.ServiceDependency(dep_str, 
        dependency = pagerduty.ServiceDependencyDependencyArgs(
            dependent_services = [pagerduty.ServiceDependencyDependencyDependentServiceArgs(
                id = dependent_service,
                type = "service"
            )],
            supporting_services = [pagerduty.ServiceDependencyDependencySupportingServiceArgs(
                id = supporting_service,
                type = "service"
            )]
        )
    )
    deps_count += 1
    dependencies[dep_str]: {
        "dependent": dependent_service,
        "supporting": supporting_service,
        "id": dep.relationships.id
    } 


def create_integration_endpoint(service_name):
    global technical_services
    int_str = f"{service_name}_int"

    integration = pagerduty.ServiceIntegration(int_str,
        type = "events_api_v2_inbound_integration",
        service = technical_services[service_name]["id"])
    technical_services[service_name]["integration_id"] = integration.id


demo_sched = pagerduty.Schedule("Pulumi Demo Sched",
            time_zone = "America/New_York",
            layers = [pagerduty.ScheduleLayerArgs(
                name = "Layer One",
                start = "2024-01-01T07:00:00-05:00",
                rotation_virtual_start = "2024-01-01T07:00:00-05:00",
                rotation_turn_length_seconds = 604800,
                users = user_ids
            )],
            teams = [demo_team_id])

demo_ep = pagerduty.EscalationPolicy("Pulumi Demo EP",
    rules = [pagerduty.EscalationPolicyRuleArgs(
        escalation_delay_in_minutes = 10,
        targets = [pagerduty.EscalationPolicyRuleTargetArgs(
            id = demo_sched.id,
            type = "schedule_reference"
        )],
    )],
    description = "Escalation Policy for Pulumi Demo",
    num_loops = 3,
    teams = demo_team_id
)

ms_demo_pulumi_biz = pagerduty.BusinessService("MicroDemo Pulumi", 
                     description = "Business Service for Microservices Demo defined by Pulumi",
                     point_of_contact = "Abby Developer",
                     team = demo_team_id)


technical_services = {
    "ms_service_fe": {
        "name": "Frontend - Pulumi Demo"},
    "ms_service_checkout": {
        "name": "Checkout - Pulumi Demo"},
    "ms_service_ads": {
        "name": "Ads - Pulumi Demo"},
    "ms_service_recommendations": {
        "name": "Recommendations - Pulumi Demo"},
    "ms_service_catalog": {
        "name": "Product Catalog - Pulumi Demo"},
    "ms_service_payment": {
        "name": "Payments - Pulumi Demo"},
    "ms_service_email": {
        "name": "Email - Pulumi Demo"},
    "ms_service_shipping": {
        "name": "Shipping - Pulumi Demo"},
    "ms_service_currency": {
        "name": "Currency - Pulumi Demo"},
    "ms_service_shoppingcart": {
        "name": "Shopping Cart - Pulumi Demo"},
    "ms_service_redis": {
        "name": "Redis Cache - Pulumi Demo"}
}   

for key in technical_services.keys():
    create_demo_service(technical_services[key])
    
# Service Dependencies

biz_to_fe = pagerduty.ServiceDependency("biz_to_fe", dependency = pagerduty.ServiceDependencyDependencyArgs(
    dependent_services = [pagerduty.ServiceDependencyDependencyDependentServiceArgs(
        id = ms_demo_pulumi_biz.id,
        type = "business_service"
    )],
    supporting_services = [pagerduty.ServiceDependencyDependencySupportingServiceArgs(
        id = technical_services["ms_service_fe"]["id"],
        type = "service",
    )],
))

relationships = {
    "ms_service_fe": ["ms_service_checkout", "ms_service_ads", "ms_service_recommendations", "ms_service_catalog", "ms_service_shoppingcart", "ms_service_shipping", "ms_service_currency"],
    "ms_service_checkout": ["ms_service_catalog", "ms_service_shoppingcart", "ms_service_shipping", "ms_service_currency", "ms_service_payment", "ms_service_email"],
    "ms_service_recommendations": ["ms_service_catalog"],
    "ms_service_shoppingcart": ["ms_service_redis"]
}

for key, values in relationships.items():
    for dep in values:
        create_tech_dep(technical_services[key]["id"], technical_services[dep]["id"])


# Service Integrations
# create one generic events API V2 integration on each service
for service_name in technical_services.keys():
    create_integration_endpoint(service_name)