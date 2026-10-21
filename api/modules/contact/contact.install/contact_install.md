# contact_install()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 70–80 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L70-L80)
- **Module/theme:** contact
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function contact_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function contact_install() {
  // Insert a default contact category.
  db_insert('contact')
    ->fields(array(
      'category' => 'Website feedback',
      'recipients' => variable_get('site_mail', ini_get('sendmail_from')),
      'selected' => 1,
      'reply' => '',
    ))
    ->execute();
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
