# user_field_extra_fields()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 214–238 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L214-L238)
- **Module/theme:** user
- **Implements:** [hook_field_extra_fields()](../../field/field.api.php/hook_field_extra_fields.md)

## Signature

```php
function user_field_extra_fields()
```

## Documentation

```text
Implements hook_field_extra_fields().
```

## Code

```php
function user_field_extra_fields() {
  $return['user']['user'] = array(
    'form' => array(
      'account' => array(
        'label' => t('User name and password'),
        'description' => t('User module account form elements.'),
        'weight' => -10,
      ),
      'timezone' => array(
        'label' => t('Timezone'),
        'description' => t('User module timezone form element.'),
        'weight' => 6,
      ),
    ),
    'display' => array(
      'summary' => array(
        'label' => t('History'),
        'description' => t('User module history view element.'),
        'weight' => 5,
      ),
    ),
  );

  return $return;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
