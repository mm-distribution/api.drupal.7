# user_entity_info()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 153–187 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L153-L187)
- **Module/theme:** user
- **Implements:** [hook_entity_info()](../../system/system.api.php/hook_entity_info.md)

## Signature

```php
function user_entity_info()
```

## Documentation

```text
Implements hook_entity_info().
```

## Code

```php
function user_entity_info() {
  $return = array(
    'user' => array(
      'label' => t('User'),
      'controller class' => 'UserController',
      'base table' => 'users',
      'uri callback' => 'user_uri',
      'label callback' => 'format_username',
      'fieldable' => TRUE,
      // $user->language is only the preferred user language for the user
      // interface textual elements. As it is not necessarily related to the
      // language assigned to fields, we do not define it as the entity language
      // key.
      'entity keys' => array(
        'id' => 'uid',
      ),
      'bundles' => array(
        'user' => array(
          'label' => t('User'),
          'admin' => array(
            'path' => 'admin/config/people/accounts',
            'access arguments' => array('administer users'),
          ),
        ),
      ),
      'view modes' => array(
        'full' => array(
          'label' => t('User account'),
          'custom settings' => FALSE,
        ),
      ),
    ),
  );
  return $return;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
