locals {
  dbre_team = ["PC6K5C9", "PULO4NW"]
  demo_team = "POJW28N"
  app_team  = ["PC6K5C9", "PULO4NW", "P73R26T"]
}

resource "pagerduty_schedule" "msd_dbre_sched" {
  name      = "DBRE Microservices Demo"
  time_zone = "America/New_York"
  layer {
    name                         = "DBREs"
    start                        = "2024-01-01T00:08:00-05:00"
    rotation_virtual_start       = "2024-01-01T00:08:00-05:00"
    rotation_turn_length_seconds = 604800
    users                        = local.dbre_team
  }

  teams = [local.demo_team]
}
resource "pagerduty_schedule" "msd_apps_sched" {
  name      = "Application Team Microservices Demo"
  time_zone = "America/New_York"
  layer {
    name                         = "Application Developers"
    start                        = "2024-01-01T00:08:00-05:00"
    rotation_virtual_start       = "2024-01-01T00:08:00-05:00"
    rotation_turn_length_seconds = 604800
    users                        = local.app_team
  }

  teams = [local.demo_team]
}