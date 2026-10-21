# system_update_7060()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2783–2907 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2783-L2907)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7060()
```

## Documentation

```text
Create fields in preparation for migrating upload.module to file.module.
```

## Code

```php
function system_update_7060() {
  if (!db_table_exists('upload')) {
    return;
  }

  if (!db_query_range('SELECT 1 FROM {upload}', 0, 1)->fetchField()) {
    // There is nothing to migrate. Delete variables and the empty table. There
    // is no need to create fields that are not going to be used.
    foreach (_update_7000_node_get_types() as $node_type) {
      variable_del('upload_' . $node_type->type);
    }
    db_drop_table('upload');
    return;
  }

  // Check which node types have upload.module attachments enabled.
  $context['types'] = array();
  foreach (_update_7000_node_get_types() as $node_type) {
    if (variable_get('upload_' . $node_type->type, 0)) {
      $context['types'][$node_type->type] = $node_type->type;
    }
  }

  // The {upload} table will be deleted when this update is complete so we
  // want to be careful to migrate all the data, even for node types that
  // may have had attachments disabled after files were uploaded. Look for
  // any other node types referenced by the upload records and add those to
  // the list. The admin can always remove the field later.
  $results = db_query('SELECT DISTINCT type FROM {node} n INNER JOIN {node_revision} nr ON n.nid = nr.nid INNER JOIN {upload} u ON nr.vid = u.vid');
  foreach ($results as $row) {
    if (!isset($context['types'][$row->type])) {
      drupal_set_message(t('The content type %rowtype had uploads disabled but contained uploaded file data. Uploads have been re-enabled to migrate the existing data. You may delete the "File attachments" field in the %rowtype type if this data is not necessary.', array('%rowtype' => $row->type)));
      $context['types'][$row->type] = $row->type;
    }
  }

  // Create a single "upload" field on all the content types that have uploads
  // enabled, then add an instance to each enabled type.
  if (count($context['types']) > 0) {
    module_enable(array('file'));
    $field = array(
      'field_name' => 'upload',
      'type' => 'file',
      'module' => 'file',
      'locked' => FALSE,
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
      'translatable' => FALSE,
      'settings' => array(
        'display_field' => 1,
        'display_default' => variable_get('upload_list_default', 1),
        'uri_scheme' => file_default_scheme(),
        'default_file' => 0,
      ),
    );

    $upload_size = variable_get('upload_uploadsize_default', 1);
    $instance = array(
      'field_name' => 'upload',
      'entity_type' => 'node',
      'bundle' => NULL,
      'label' => 'File attachments',
      'required' => 0,
      'description' => '',
      'widget' => array(
        'weight' => '1',
        'settings' => array(
          'progress_indicator' => 'throbber',
        ),
        'type' => 'file_generic',
      ),
      'settings' => array(
        'max_filesize' => $upload_size ? ($upload_size . ' MB') : '',
        'file_extensions' => variable_get('upload_extensions_default', 'jpg jpeg gif png txt doc xls pdf ppt pps odt ods odp'),
        'file_directory' => '',
        'description_field' => 1,
      ),
      'display' => array(
        'default' => array(
          'label' => 'hidden',
          'type' => 'file_table',
          'settings' => array(),
          'weight' => 0,
          'module' => 'file',
        ),
        'full' => array(
          'label' => 'hidden',
          'type' => 'file_table',
          'settings' => array(),
          'weight' => 0,
          'module' => 'file',
        ),
        'teaser' => array(
          'label' => 'hidden',
          'type' => 'hidden',
          'settings' => array(),
          'weight' => 0,
          'module' => NULL,
        ),
        'rss' => array(
          'label' => 'hidden',
          'type' => 'file_table',
          'settings' => array(),
          'weight' => 0,
          'module' => 'file',
        ),
      ),
    );

    // Create the field.
    _update_7000_field_create_field($field);

    // Create the instances.
    foreach ($context['types'] as $bundle) {
      $instance['bundle'] = $bundle;
      _update_7000_field_create_instance($field, $instance);
      // Now that the instance is created, we can safely delete any legacy
      // node type information.
      variable_del('upload_' . $bundle);
    }
  }
  else {
    // No uploads or content types with uploads enabled.
    db_drop_table('upload');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
