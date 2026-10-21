# contact_permission()

- **Type:** Function
- **File:** [`modules/contact/contact.module`](_file.md), lines 40–52 · [local source](../../../../source/modules/contact/contact.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module#L40-L52)
- **Module/theme:** contact
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function contact_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function contact_permission() {
  return array(
    'administer contact forms' => array(
      'title' => t('Administer contact forms and contact form settings'),
    ),
    'access site-wide contact form' => array(
      'title' => t('Use the site-wide contact form'),
    ),
    'access user contact forms' => array(
      'title' => t("Use users' personal contact forms"),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/contact/contact.module](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.module) · Licensed GPL-2.0-or-later (see LICENSE)._
