# forum_update_7003()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 370–442 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L370-L442)
- **Module/theme:** forum
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function forum_update_7003()
```

## Documentation

```text
Rename field to 'taxonomy_forums'.
```

## Code

```php
function forum_update_7003() {
  $messages = array();

  $new_field_name = 'taxonomy_forums';

  // Test to see if the taxonomy_forums field exists.
  $fields = _update_7000_field_read_fields(array('field_name' => $new_field_name));
  if ($fields) {
    // Since the field exists, we're done.
    return;
  }

  // Calculate the old field name.
  $vid = variable_get('forum_nav_vocabulary', 0);
  $vocabulary_machine_name = db_select('taxonomy_vocabulary', 'tv')
    ->fields('tv', array('machine_name'))
    ->condition('vid', $vid)
    ->execute()
    ->fetchField();
  $old_field_name = 'taxonomy_' . $vocabulary_machine_name;

  // Read the old fields.
  $old_fields = _update_7000_field_read_fields(array('field_name' => $old_field_name));
  foreach ($old_fields as $old_field) {
    if ($old_field['storage']['type'] != 'field_sql_storage') {
      $messages[] = t('Cannot rename field %id (%old_field_name) to %new_field_name because it does not use the field_sql_storage storage type.', array(
        '%id' => $old_field['id'],
        '%old_field_name' => $old_field_name,
        '%new_field_name' => $new_field_name,
      ));
      continue;
    }

    // Update {field_config}.
    db_update('field_config')
      ->fields(array('field_name' => $new_field_name))
      ->condition('id', $old_field['id'])
      ->execute();

    // Update {field_config_instance}.
    db_update('field_config_instance')
      ->fields(array('field_name' => $new_field_name))
      ->condition('field_id', $old_field['id'])
      ->execute();

    // The tables that need updating in the form 'old_name' => 'new_name'.
    $tables = array(
      'field_data_' . $old_field_name => 'field_data_' . $new_field_name,
      'field_revision_' . $old_field_name => 'field_revision_' . $new_field_name,
    );
    foreach ($tables as $old_table => $new_table) {
      $old_column_name = $old_field_name . '_tid';
      $new_column_name = $new_field_name . '_tid';

      // Rename the column.
      db_drop_index($old_table, $old_column_name);
      db_change_field($old_table, $old_column_name, $new_column_name, array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => FALSE,
      ));
      db_drop_index($old_table, $new_column_name);
      db_add_index($old_table, $new_column_name, array($new_column_name));

      // Rename the table.
      db_rename_table($old_table, $new_table);
    }
  }

  cache_clear_all('*', 'cache_field', TRUE);

  return $messages;
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
