# path_admin_overview()

- **Type:** Function
- **File:** [`modules/path/path.admin.inc`](_file.md), lines 14–91 · [local source](../../../../source/modules/path/path.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc#L14-L91)
- **Module/theme:** path

## Signature

```php
function path_admin_overview()
```

## Documentation

```text
Returns a listing of all defined URL aliases.

When filter key passed, perform a standard search on the given key,
and return the list of matching URL aliases.
```

## Code

```php
function path_admin_overview() {
  // Get search keys.
  $args = func_get_args();
  $keys = implode('/', $args);

  // Add the filter form above the overview table.
  $build['path_admin_filter_form'] = drupal_get_form('path_admin_filter_form', $keys);
  // Enable language column if locale is enabled or if we have any alias with language
  $alias_exists = (bool) db_query_range('SELECT 1 FROM {url_alias} WHERE language <> :language', 0, 1, array(':language' => LANGUAGE_NONE))->fetchField();
  $multilanguage = (module_exists('locale') || $alias_exists);

  $header = array();
  $header[] = array('data' => t('Alias'), 'field' => 'alias', 'sort' => 'asc');
  $header[] = array('data' => t('System'), 'field' => 'source');
  if ($multilanguage) {
    $header[] = array('data' => t('Language'), 'field' => 'language');
  }
  $header[] = array('data' => t('Operations'));

  $query = db_select('url_alias')->extend('PagerDefault')->extend('TableSort');
  if ($keys) {
    // Replace wildcards with PDO wildcards.
    $query->condition('alias', '%' . preg_replace('!\*+!', '%', $keys) . '%', 'LIKE');
  }
  $result = $query
    ->fields('url_alias')
    ->orderByHeader($header)
    ->limit(50)
    ->execute();

  $rows = array();
  $destination = drupal_get_destination();
  foreach ($result as $data) {
    $row = array();
    $row['data']['alias'] = l($data->alias, $data->source);
    $row['data']['source'] = l($data->source, $data->source, array('alias' => TRUE));
    if ($multilanguage) {
      $row['data']['language'] = module_invoke('locale', 'language_name', $data->language);
    }

    $operations = array();
    $operations['edit'] = array(
      'title' => t('edit'),
      'href' => "admin/config/search/path/edit/$data->pid",
      'query' => $destination,
    );
    $operations['delete'] = array(
      'title' => t('delete'),
      'href' => "admin/config/search/path/delete/$data->pid",
      'query' => $destination,
    );
    $row['data']['operations'] = array(
      'data' => array(
        '#theme' => 'links',
        '#links' => $operations,
        '#attributes' => array('class' => array('links', 'inline', 'nowrap')),
      ),
    );

    // If the system path maps to a different URL alias, highlight this table
    // row to let the user know of old aliases.
    if ($data->alias != drupal_get_path_alias($data->source, $data->language)) {
      $row['class'] = array('warning');
    }

    $rows[] = $row;
  }

  $build['path_table'] = array(
    '#theme' => 'table',
    '#header' => $header,
    '#rows' => $rows,
    '#empty' => t('No URL aliases available. <a href="@link">Add URL alias</a>.', array('@link' => url('admin/config/search/path/add'))),
  );
  $build['path_pager'] = array('#theme' => 'pager');

  return $build;
}
```

---
_Drupal 7.103 · [modules/path/path.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/path/path.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
