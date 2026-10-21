# contact_uninstall()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 85–89 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L85-L89)
- **Module/theme:** contact
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function contact_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function contact_uninstall() {
  variable_del('contact_default_status');
  variable_del('contact_threshold_limit');
  variable_del('contact_threshold_window');
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
