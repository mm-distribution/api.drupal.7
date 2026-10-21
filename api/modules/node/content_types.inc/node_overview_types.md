# node_overview_types()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 11–54 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L11-L54)
- **Module/theme:** node

## Signature

```php
function node_overview_types()
```

## Documentation

```text
Displays the content type admin overview page.
```

## Code

```php
function node_overview_types() {
  $types = node_type_get_types();
  $names = node_type_get_names();
  $field_ui = module_exists('field_ui') && user_access('administer fields');
  $header = array(t('Name'), array('data' => t('Operations'), 'colspan' => $field_ui ? '4' : '2'));
  $rows = array();

  foreach ($names as $key => $name) {
    $type = $types[$key];
    if (node_hook($type->type, 'form')) {
      $type_url_str = str_replace('_', '-', $type->type);
      $row = array(theme('node_admin_overview', array('name' => $name, 'type' => $type)));
      // Set the edit column.
      $row[] = array('data' => l(t('edit'), 'admin/structure/types/manage/' . $type_url_str));

      if ($field_ui) {
        // Manage fields.
        $row[] = array('data' => l(t('manage fields'), 'admin/structure/types/manage/' . $type_url_str . '/fields'));

        // Display fields.
        $row[] = array('data' => l(t('manage display'), 'admin/structure/types/manage/' . $type_url_str . '/display'));
      }

      // Set the delete column.
      if ($type->custom) {
        $row[] = array('data' => l(t('delete'), 'admin/structure/types/manage/' . $type_url_str . '/delete'));
      }
      else {
        $row[] = array('data' => '');
      }

      $rows[] = $row;
    }
  }

  $build['node_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No content types available. <a href="@link">Add content type</a>.', array('@link' => url('admin/structure/types/add'))),
  );

  return $build;
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
