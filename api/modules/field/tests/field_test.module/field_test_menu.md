# field_test_menu()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.module`](_file.md), lines 40–71 · [local source](../../../../../source/modules/field/tests/field_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module#L40-L71)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_menu()](../../../system/system.api.php/hook_menu.md)

## Signature

```php
function field_test_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function field_test_menu() {
  $items = array();
  $bundles = field_info_bundles('test_entity');

  foreach ($bundles as $bundle_name => $bundle_info) {
    $bundle_url_str = str_replace('_', '-', $bundle_name);
    $items['test-entity/add/' . $bundle_url_str] = array(
      'title' => t('Add %bundle test_entity', array('%bundle' => $bundle_info['label'])),
      'page callback' => 'field_test_entity_add',
      'page arguments' => array(2),
      'access arguments' => array('administer field_test content'),
      'type' => MENU_NORMAL_ITEM,
    );
  }
  $items['test-entity/manage/%field_test_entity_test/edit'] = array(
    'title' => 'Edit test entity',
    'page callback' => 'field_test_entity_edit',
    'page arguments' => array(2),
    'access arguments' => array('administer field_test content'),
    'type' => MENU_NORMAL_ITEM,
  );

  $items['test-entity/nested/%field_test_entity_test/%field_test_entity_test'] = array(
    'title' => 'Nested entity form',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('field_test_entity_nested_form', 2, 3),
    'access arguments' => array('administer field_test content'),
    'type' => MENU_NORMAL_ITEM,
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.module](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
