resource "pagerduty_escalation_policy" "msd_dbre" {
    name = "DBRE Microservices Demo"
    num_loops = 1
    teams = [local.demo_team]
    rule {
        escalation_delay_in_minutes = 10
        target {
            type = "schedule_reference"
            id = pagerduty_schedule.msd_dbre_sched.id
        }
    }
}

resource "pagerduty_escalation_policy" "msd_apps" {
    name = "Application Team Microservices Demo"
    num_loops = 1
    teams = [local.demo_team]
    rule {
        escalation_delay_in_minutes = 10
        target {
            type = "schedule_reference"
            id = pagerduty_schedule.msd_apps_sched.id
        }
    }
}