# contact_update_7000()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 118–121 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L118-L121)
- **Module/theme:** contact
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function contact_update_7000()
```

## Documentation

```text
Rename the threshold limit variable.
```

## Code

```php
function contact_update_7000() {
  variable_set('contact_threshold_limit', variable_get('contact_hourly_threshold', 5));
  variable_del('contact_hourly_threshold');
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
