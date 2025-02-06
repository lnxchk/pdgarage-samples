# services, bottom to top
# Redis Cache
resource "pagerduty_service" "Demo_Redis_Cache" {
  name              = "Redis Cache - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_dbre.id
  alert_creation    = "create_alerts_and_incidents"
}

# Shopping Cart
resource "pagerduty_service" "Demo_Cart" {
  name              = "Shopping Cart - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Product Catalog
resource "pagerduty_service" "Demo_Catalog" {
  name              = "Product Catalog - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Shipping
resource "pagerduty_service" "Demo_Shipping" {
  name              = "Shipping - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Currency Converter
resource "pagerduty_service" "Demo_Currency" {
  name              = "Currency Converter - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Ad Service
resource "pagerduty_service" "Demo_Ads" {
  name              = "Ads Service - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Recommendations
resource "pagerduty_service" "Demo_Recs" {
  name              = "Recommendation Service - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Payments
resource "pagerduty_service" "Demo_Payments" {
  name              = "Payments Service - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Email
resource "pagerduty_service" "Demo_Email" {
  name              = "Email Service - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Checkout
resource "pagerduty_service" "Demo_Checkout" {
  name              = "Checkout Service - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"
}

# Frontend
resource "pagerduty_service" "Demo_Frontend" {
  name              = "Frontend - Microservices Demo"
  escalation_policy = pagerduty_escalation_policy.msd_apps.id
  alert_creation    = "create_alerts_and_incidents"

}

# Business service
resource "pagerduty_business_service" "Microservices_Demo" {
  name        = "Microservices Demo"
  description = "Services aligned behind the Online Boutique Demo"
  team        = local.demo_team
}