# contact_update_7003()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 152–164 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L152-L164)
- **Module/theme:** contact
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function contact_update_7003()
```

## Documentation

```text
Change the weight column to normal int.
```

## Code

```php
function contact_update_7003() {
  db_drop_index('contact', 'list');
  db_change_field('contact', 'weight', 'weight', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => "The category's weight.",
  ), array(
    'indexes' => array(
      'list' => array('weight', 'category'),
    ),
  ));
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
