# modules/poll/poll.install

- **Source:** [local](../../../../source/modules/poll/poll.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/poll/poll.install) · 216 lines
- **Module/theme:** poll

## File documentation

```text
@file
Install, update and uninstall functions for the poll module.
```

## Functions (derived index)

- [poll_schema()](poll_schema.md) — Implements hook_schema().
- [poll_update_7001()](poll_update_7001.md) — Use the poll_choice primary key to record votes in poll_votes rather than the choice order. Rename chorder to weight.
- [poll_update_7002()](poll_update_7002.md) — Add timestamp field to {poll_vote}.
- [poll_update_7003()](poll_update_7003.md) — Change the weight column to normal int.
- [poll_update_7004()](poll_update_7004.md) — Update the database to match the schema.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
