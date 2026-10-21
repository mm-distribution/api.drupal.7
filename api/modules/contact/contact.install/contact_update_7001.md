# contact_update_7001()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 126–131 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L126-L131)
- **Module/theme:** contact
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function contact_update_7001()
```

## Documentation

```text
Rename the administer contact forms permission.
```

## Code

```php
function contact_update_7001() {
  db_update('role_permission')
    ->fields(array('permission' => 'administer contact forms'))
    ->condition('permission', 'administer site-wide contact form')
    ->execute();
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
