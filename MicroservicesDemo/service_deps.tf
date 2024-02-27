resource "pagerduty_service_dependency" "biz_to_fe" {
    dependency {
        dependent_service {
            id = pagerduty_business_service.Microservices_Demo.id
            type = pagerduty_business_service.Microservices_Demo.type
        }

        supporting_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
    }
}
resource "pagerduty_service_dependency" "fe_to_checkout" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Checkout.id
            type = pagerduty_service.Demo_Checkout.type
        }
    }
}

resource "pagerduty_service_dependency" "fe_to_ads" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Ads.id
            type = pagerduty_service.Demo_Ads.type
        }
    }
}

resource "pagerduty_service_dependency" "fe_to_recs" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Recs.id
            type = pagerduty_service.Demo_Recs.type
        }
    }
}

resource "pagerduty_service_dependency" "fe_to_catalog" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Catalog.id
            type = pagerduty_service.Demo_Catalog.type
        }
    }
}

resource "pagerduty_service_dependency" "fe_to_cart" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Cart.id
            type = pagerduty_service.Demo_Cart.type
        }
    }
}

resource "pagerduty_service_dependency" "fe_to_shipping" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Shipping.id
            type = pagerduty_service.Demo_Shipping.type
        }
    }
}

resource "pagerduty_service_dependency" "fe_to_currency" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Frontend.id
            type = pagerduty_service.Demo_Frontend.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Currency.id
            type = pagerduty_service.Demo_Currency.type
        }
    }
}

resource "pagerduty_service_dependency" "checkout_to_catalog" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Checkout.id
            type = pagerduty_service.Demo_Checkout.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Catalog.id
            type = pagerduty_service.Demo_Catalog.type
        }
    }
}

resource "pagerduty_service_dependency" "checkout_to_cart" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Checkout.id
            type = pagerduty_service.Demo_Checkout.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Cart.id
            type = pagerduty_service.Demo_Cart.type
        }
    }
}

resource "pagerduty_service_dependency" "checkout_to_shipping" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Checkout.id
            type = pagerduty_service.Demo_Checkout.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Shipping.id
            type = pagerduty_service.Demo_Shipping.type
        }
    }
}

resource "pagerduty_service_dependency" "checkout_to_currency" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Checkout.id
            type = pagerduty_service.Demo_Checkout.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Currency.id
            type = pagerduty_service.Demo_Currency.type
        }
    }
}

resource "pagerduty_service_dependency" "checkout_to_payments" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Checkout.id
            type = pagerduty_service.Demo_Checkout.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Payments.id
            type = pagerduty_service.Demo_Payments.type
        }
    }
}

resource "pagerduty_service_dependency" "checkout_to_email" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Checkout.id
            type = pagerduty_service.Demo_Checkout.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Email.id
            type = pagerduty_service.Demo_Email.type
        }
    }
}

resource "pagerduty_service_dependency" "recs_to_catalog" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Recs.id
            type = pagerduty_service.Demo_Recs.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Catalog.id
            type = pagerduty_service.Demo_Catalog.type
        }
    }
}

resource "pagerduty_service_dependency" "cart_to_cache" {
    dependency {
        dependent_service {
            id = pagerduty_service.Demo_Cart.id
            type = pagerduty_service.Demo_Cart.type
        }
        supporting_service {
            id = pagerduty_service.Demo_Redis_Cache.id
            type = pagerduty_service.Demo_Redis_Cache.type
        }
    }
}