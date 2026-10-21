# user_block_configure()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1406–1425 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1406-L1425)
- **Module/theme:** user
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function user_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function user_block_configure($delta = '') {
  global $user;

  switch ($delta) {
    case 'new':
      $form['user_block_whois_new_count'] = array(
        '#type' => 'select',
        '#title' => t('Number of users to display'),
        '#default_value' => variable_get('user_block_whois_new_count', 5),
        '#options' => drupal_map_assoc(array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)),
      );
      return $form;

    case 'online':
      $period = drupal_map_assoc(array(30, 60, 120, 180, 300, 600, 900, 1800, 2700, 3600, 5400, 7200, 10800, 21600, 43200, 86400), 'format_interval');
      $form['user_block_seconds_online'] = array('#type' => 'select', '#title' => t('User activity'), '#default_value' => variable_get('user_block_seconds_online', 900), '#options' => $period, '#description' => t('A user is considered online for this long after they have last viewed a page.'));
      $form['user_block_max_list_count'] = array('#type' => 'select', '#title' => t('User list length'), '#default_value' => variable_get('user_block_max_list_count', 10), '#options' => drupal_map_assoc(array(0, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100)), '#description' => t('Maximum number of currently online users to display.'));
      return $form;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
