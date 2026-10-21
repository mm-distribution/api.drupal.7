# system_actions_manage()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 3001–3054 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L3001-L3054)
- **Module/theme:** system

## Signature

```php
function system_actions_manage()
```

## Documentation

```text
Menu callback; Displays an overview of available and configured actions.
```

## Code

```php
function system_actions_manage() {
  actions_synchronize();
  $actions = actions_list();
  $actions_map = actions_actions_map($actions);
  $options = array();
  $unconfigurable = array();

  foreach ($actions_map as $key => $array) {
    if ($array['configurable']) {
      $options[$key] = $array['label'] . '...';
    }
    else {
      $unconfigurable[] = $array;
    }
  }

  $row = array();
  $instances_present = db_query("SELECT aid FROM {actions} WHERE parameters <> ''")->fetchField();
  $header = array(
    array('data' => t('Action type'), 'field' => 'type'),
    array('data' => t('Label'), 'field' => 'label'),
    array('data' => $instances_present ? t('Operations') : '', 'colspan' => '2')
  );
  $query = db_select('actions')->extend('PagerDefault')->extend('TableSort');
  $result = $query
    ->fields('actions')
    ->limit(50)
    ->orderByHeader($header)
    ->execute();

  foreach ($result as $action) {
    $row[] = array(
      array('data' => $action->type),
      array('data' => check_plain($action->label)),
      array('data' => $action->parameters ? l(t('configure'), "admin/config/system/actions/configure/$action->aid") : ''),
      array('data' => $action->parameters ? l(t('delete'), "admin/config/system/actions/delete/$action->aid") : '')
    );
  }

  if ($row) {
    $pager = theme('pager');
    if (!empty($pager)) {
      $row[] = array(array('data' => $pager, 'colspan' => '3'));
    }
    $build['system_actions_header'] = array('#markup' => '<h3>' . t('Available actions:') . '</h3>');
    $build['system_actions_table'] = array('#markup' => theme('table', array('header' => $header, 'rows' => $row)));
  }

  if ($actions_map) {
    $build['system_actions_manage_form'] = drupal_get_form('system_actions_manage_form', $options);
  }

  return $build;
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
