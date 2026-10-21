# system_update_7087()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3438–3442 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3438-L3442)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7087()
```

## Documentation

```text
Enable the Announcements module; see 7.100 Release Notes for opt-out details.
```

## Code

```php
function system_update_7087() {
  if (!variable_get('announcements_feed_enable_by_default_opt_out', FALSE)) {
    module_enable(array('announcements_feed'), FALSE);
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
