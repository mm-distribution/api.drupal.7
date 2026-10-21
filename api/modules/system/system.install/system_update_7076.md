# system_update_7076()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 3268–3285 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L3268-L3285)
- **Module/theme:** system
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function system_update_7076()
```

## Documentation

```text
Convert menu_links query strings into arrays.
```

## Code

```php
function system_update_7076() {
  $query = db_select('menu_links', 'ml', array('fetch' => PDO::FETCH_ASSOC))
    ->fields('ml', array('mlid', 'options'));
  foreach ($query->execute() as $menu_link) {
    if (strpos($menu_link['options'], 'query') !== FALSE) {
      $menu_link['options'] = unserialize($menu_link['options']);
      if (isset($menu_link['options']['query']) && is_string($menu_link['options']['query'])) {
        $menu_link['options']['query'] = drupal_get_query_array($menu_link['options']['query']);
        db_update('menu_links')
          ->fields(array(
            'options' => serialize($menu_link['options']),
          ))
          ->condition('mlid', $menu_link['mlid'], '=')
          ->execute();
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
