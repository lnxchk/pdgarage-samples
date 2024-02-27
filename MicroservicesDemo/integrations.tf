resource "pagerduty_service_integration" "events_msd_frontend" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Frontend.id
}

resource "pagerduty_service_integration" "events_msd_checkout" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Checkout.id
}

resource "pagerduty_service_integration" "events_msd_ads" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Ads.id
}

resource "pagerduty_service_integration" "events_msd_recs" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Recs.id
}

resource "pagerduty_service_integration" "events_msd_payments" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Payments.id
}

resource "pagerduty_service_integration" "events_msd_email" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Email.id
}

resource "pagerduty_service_integration" "events_msd_catalog" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Catalog.id
}

resource "pagerduty_service_integration" "events_msd_shipping" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Shipping.id
}

resource "pagerduty_service_integration" "events_msd_currency" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Currency.id
}

resource "pagerduty_service_integration" "events_msd_cart" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Cart.id
}

resource "pagerduty_service_integration" "events_msd_redis" {
    name = "API V2"
    type = "events_api_v2_inbound_integration"
    service = pagerduty_service.Demo_Redis_Cache.id
}