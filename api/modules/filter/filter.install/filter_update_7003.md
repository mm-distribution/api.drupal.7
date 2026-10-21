# filter_update_7003()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 222–342 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L222-L342)
- **Module/theme:** filter
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function filter_update_7003()
```

## Documentation

```text
Upgrade the {filter} table for core filters.
```

## Code

```php
function filter_update_7003() {
  // Duplicates the {filters} table since core cannot take care of the potential
  // contributed module filters.
  db_rename_table('filters', 'd6_upgrade_filter');
  // Creates the Drupal 7 filter table.
  $filter_table =  array(
    'description' => 'Table that maps filters (HTML corrector) to text formats (Filtered HTML).',
    'fields' => array(
      'format' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Foreign key: The {filter_format}.format to which this filter is assigned.',
      ),
      'module' => array(
        'type' => 'varchar',
        'length' => 64,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The origin module of the filter.',
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Name of the filter being referenced.',
      ),
      'weight' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Weight of filter within format.',
      ),
      'status' => array(
        'type' => 'int',
        'not null' => TRUE,
        'default' => 0,
        'description' => 'Filter enabled status. (1 = enabled, 0 = disabled)',
      ),
      'settings' => array(
        'type' => 'blob',
        'not null' => FALSE,
        'size' => 'big',
        'serialize' => TRUE,
        'description' => 'A serialized array of name value pairs that store the filter settings for the specific format.',
      ),
    ),
    'primary key' => array('format', 'name'),
    'indexes' => array(
      'list' => array('weight', 'module', 'name'),
    ),
  );
  db_create_table('filter', $filter_table);

  // Get an array of the renamed filter deltas, organized by module.
  $renamed_deltas = array(
    'filter' => array(
      '0' => 'filter_html',
      '1' => 'filter_autop',
      '2' => 'filter_url',
      '3' => 'filter_htmlcorrector',
      '4' => 'filter_html_escape',
    ),
    'php' => array(
      '0' => 'php_code',
    ),
  );

  // Loop through each filter and make changes to the core filter table by
  // each record from the old to the new table.
  foreach ($renamed_deltas as $module => $deltas) {
    foreach ($deltas as $old_delta => $new_name) {
      $query = db_select('d6_upgrade_filter')
        ->fields('d6_upgrade_filter', array('format', 'weight'))
        ->condition('module', $module)
        ->condition('delta', $old_delta)
        ->distinct();

      foreach ($query->execute() as $record) {
        // Port the filter settings.
        $settings = array();
        if ($new_name == 'filter_html') {
          if ($setting = variable_get("allowed_html_{$record->format}", NULL)) {
            $settings['allowed_html'] = $setting;
            variable_del("allowed_html_{$record->format}");
          }
          if ($setting = variable_get("filter_html_help_{$record->format}", NULL)) {
            $settings['filter_html_help'] = $setting;
            variable_del("filter_html_help_{$record->format}");
          }
          if ($setting = variable_get("filter_html_nofollow_{$record->format}", NULL)) {
            $settings['filter_html_nofollow'] = $setting;
            variable_del("filter_html_nofollow_{$record->format}");
          }
        }
        elseif ($new_name == 'filter_url') {
          if ($setting = variable_get("filter_url_length_{$record->format}", NULL)) {
            $settings['filter_url_length'] = $setting;
            variable_del("filter_url_length_{$record->format}");
          }
        }

        db_insert('filter')
          ->fields(array(
            'format' => $record->format,
            'module' => $module,
            'name' => $new_name,
            'weight' => $record->weight,
            'settings' => serialize($settings),
            'status' => 1,
          ))
          ->execute();
      }
      db_delete('d6_upgrade_filter')
        ->condition('module', $module)
        ->condition('delta', $old_delta)
        ->execute();
    }
  }
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
