# field_help()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 284–317 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L284-L317)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function field_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function field_help($path, $arg) {
  switch ($path) {
    case 'admin/help#field':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Field module allows custom data fields to be defined for <em>entity</em> types (entities include content items, comments, user accounts, and taxonomy terms). The Field module takes care of storing, loading, editing, and rendering field data. Most users will not interact with the Field module directly, but will instead use the <a href="@field-ui-help">Field UI module</a> user interface. Module developers can use the Field API to make new entity types "fieldable" and thus allow fields to be attached to them. For more information, see the online handbook entry for <a href="@field">Field module</a>.', array('@field-ui-help' => url('admin/help/field_ui'), '@field' => 'http://drupal.org/documentation/modules/field')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Enabling field types') . '</dt>';
      $output .= '<dd>' . t('The Field module provides the infrastructure for fields and field attachment; the field types and input widgets themselves are provided by additional modules. Some of the modules are required; the optional modules can be enabled from the <a href="@modules">Modules administration page</a>. Drupal core includes the following field type modules: Number (required), Text (required), List (required), Taxonomy (optional), Image (optional), and File (optional); the required Options module provides input widgets for other field modules. Additional fields and widgets may be provided by contributed modules, which you can find in the <a href="@contrib">contributed module section of Drupal.org</a>. Currently enabled field and input widget modules:', array('@modules' => url('admin/modules'), '@contrib' => 'http://drupal.org/project/modules', '@options' => url('admin/help/options')));

      // Make a list of all widget and field modules currently enabled, in
      // order by displayed module name (module names are not translated).
      $items = array();
      $info = system_get_info('module');
      $modules = array_merge(module_implements('field_info'), module_implements('field_widget_info'));
      $modules = array_unique($modules);
      sort($modules);
      foreach ($modules as $module) {
        $display = $info[$module]['name'];
        if (module_hook($module, 'help')) {
          $items['items'][] = l($display, 'admin/help/' . $module);
        }
        else {
          $items['items'][] = $display;
        }
      }
      $output .= theme('item_list', $items) . '</dd>';
      $output .= '<dt>' . t('Managing field data storage') . '</dt>';
      $output .= '<dd>' . t('Developers of field modules can either use the default <a href="@sql-store">Field SQL storage module</a> to store data for their fields, or a contributed or custom module developed using the <a href="@storage-api">field storage API</a>.', array('@storage-api' => 'http://api.drupal.org/api/group/field_storage/7', '@sql-store' => url('admin/help/field_sql_storage'))) . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
