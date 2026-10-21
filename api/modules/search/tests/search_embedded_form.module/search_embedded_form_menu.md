# search_embedded_form_menu()

- **Type:** Function
- **File:** [`modules/search/tests/search_embedded_form.module`](_file.md), lines 15–25 · [local source](../../../../../source/modules/search/tests/search_embedded_form.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module#L15-L25)
- **Module/theme:** search_node_tags
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function search_embedded_form_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function search_embedded_form_menu() {
  $items['search_embedded_form'] = array(
    'title' => 'Search_Embed_Form',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('search_embedded_form_form'),
    'access arguments' => array('search content'),
    'type' => MENU_CALLBACK,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/search/tests/search_embedded_form.module](https://github.com/drupal/drupal/blob/7.103/modules/search/tests/search_embedded_form.module) · Licensed GPL-2.0-or-later (see LICENSE)._
