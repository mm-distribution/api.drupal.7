# system_update_7061()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2912–3087 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2912-L3087)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7061(&$sandbox)
```

## Documentation

```text
Migrate upload.module data to the newly created file field.
```

## Code

```php
function system_update_7061(&$sandbox) {
  if (!db_table_exists('upload')) {
    return;
  }

  if (!isset($sandbox['progress'])) {
    // Delete stale rows from {upload} where the fid is not in the {files} table.
    db_delete('upload')
      ->notExists(
        db_select('files', 'f')
        ->fields('f', array('fid'))
        ->where('f.fid = {upload}.fid')
      )
      ->execute();

    // Delete stale rows from {upload} where the vid is not in the
    // {node_revision} table. The table has already been renamed in
    // node_update_7001().
    db_delete('upload')
      ->notExists(
        db_select('node_revision', 'nr')
        ->fields('nr', array('vid'))
        ->where('nr.vid = {upload}.vid')
      )
      ->execute();

    // Retrieve a list of node revisions that have uploaded files attached.
    // DISTINCT queries are expensive, especially when paged, so we store the
    // data in its own table for the duration of the update.
    if (!db_table_exists('system_update_7061')) {
      $table = array(
        'description' => t('Stores temporary data for system_update_7061.'),
        'fields' => array('vid' => array('type' => 'int', 'not null' => TRUE)),
        'primary key' => array('vid'),
      );
      db_create_table('system_update_7061', $table);
    }
    $query = db_select('upload', 'u');
    $query->distinct();
    $query->addField('u','vid');
    db_insert('system_update_7061')
      ->from($query)
      ->execute();

    // Retrieve a list of duplicate files with the same filepath. Only the
    // most-recently uploaded of these will be moved to the new {file_managed}
    // table (and all references will be updated to point to it), since
    // duplicate file URIs are not allowed in Drupal 7.
    // Since the Drupal 6 to 7 upgrade path leaves the {files} table behind
    // after it's done, custom or contributed modules which need to migrate
    // file references of their own can use a similar query to determine the
    // file IDs that duplicate filepaths were mapped to.
    $sandbox['duplicate_filepath_fids_to_use'] = db_query("SELECT filepath, MAX(fid) FROM {files} GROUP BY filepath HAVING COUNT(*) > 1")->fetchAllKeyed();

    // Initialize batch update information.
    $sandbox['progress'] = 0;
    $sandbox['last_vid_processed'] = -1;
    $sandbox['max'] = db_query("SELECT COUNT(*) FROM {system_update_7061}")->fetchField();
  }

  // Determine vids for this batch.
  // Process all files attached to a given revision during the same batch.
  $limit = variable_get('upload_update_batch_size', 100);
  $vids = db_query_range('SELECT vid FROM {system_update_7061} WHERE vid > :lastvid ORDER BY vid', 0, $limit, array(':lastvid' => $sandbox['last_vid_processed']))
    ->fetchCol();

  // Retrieve information on all the files attached to these revisions.
  if (!empty($vids)) {
    $node_revisions = array();
    $result = db_query('SELECT u.fid, u.vid, u.list, u.description, n.nid, n.type, u.weight FROM {upload} u INNER JOIN {node_revision} nr ON u.vid = nr.vid INNER JOIN {node} n ON n.nid = nr.nid WHERE u.vid IN (:vids) ORDER BY u.vid, u.weight, u.fid', array(':vids' => $vids));
    foreach ($result as $record) {
      // For each uploaded file, retrieve the corresponding data from the old
      // files table (since upload doesn't know about the new entry in the
      // file_managed table).
      $file = db_select('files', 'f')
        ->fields('f', array('fid', 'uid', 'filename', 'filepath', 'filemime', 'filesize', 'status', 'timestamp'))
        ->condition('f.fid', $record->fid)
        ->execute()
        ->fetchAssoc();
      if (!$file) {
        continue;
      }

      // If this file has a duplicate filepath, replace it with the
      // most-recently uploaded file that has the same filepath.
      if (isset($sandbox['duplicate_filepath_fids_to_use'][$file['filepath']]) && $record->fid != $sandbox['duplicate_filepath_fids_to_use'][$file['filepath']]) {
        $file = db_select('files', 'f')
          ->fields('f', array('fid', 'uid', 'filename', 'filepath', 'filemime', 'filesize', 'status', 'timestamp'))
          ->condition('f.fid', $sandbox['duplicate_filepath_fids_to_use'][$file['filepath']])
          ->execute()
          ->fetchAssoc();
      }

      // Add in the file information from the upload table.
      $file['description'] = $record->description;
      $file['display'] = $record->list;

      // Create one record for each revision that contains all the uploaded
      // files.
      $node_revisions[$record->vid]['nid'] = $record->nid;
      $node_revisions[$record->vid]['vid'] = $record->vid;
      $node_revisions[$record->vid]['type'] = $record->type;
      $node_revisions[$record->vid]['file'][LANGUAGE_NONE][] = $file;
    }

    // Now that we know which files belong to which revisions, update the
    // files'// database entries, and save a reference to each file in the
    // upload field on their node revisions.
    $basename = variable_get('file_directory_path', conf_path() . '/files');
    $scheme = file_default_scheme() . '://';
    foreach ($node_revisions as $vid => $revision) {
      foreach ($revision['file'][LANGUAGE_NONE] as $delta => $file) {
        // We will convert filepaths to URI using the default scheme
        // and stripping off the existing file directory path.
        $file['uri'] = $scheme . preg_replace('!^' . preg_quote($basename) . '!', '', $file['filepath']);
        // Normalize the URI but don't call file_stream_wrapper_uri_normalize()
        // directly, since that is a higher-level API function which invokes
        // hooks while validating the scheme, and those will not work during
        // the upgrade. Instead, use a simpler version that just assumes the
        // scheme from above is already valid.
        if (($file_uri_scheme = file_uri_scheme($file['uri'])) && ($file_uri_target = file_uri_target($file['uri']))) {
          $file['uri'] = $file_uri_scheme . '://' . $file_uri_target;
        }
        unset($file['filepath']);
        // Insert into the file_managed table.
        // Each fid should only be stored once in file_managed.
        db_merge('file_managed')
          ->key(array(
            'fid' => $file['fid'],
          ))
          ->fields(array(
            'uid' => $file['uid'],
            'filename' => $file['filename'],
            'uri' => $file['uri'],
            'filemime' => $file['filemime'],
            'filesize' => $file['filesize'],
            'status' => $file['status'],
            'timestamp' => $file['timestamp'],
          ))
          ->execute();

        // Add the usage entry for the file.
        $file = (object) $file;
        file_usage_add($file, 'file', 'node', $revision['nid']);

        // Update the node revision's upload file field with the file data.
        $revision['file'][LANGUAGE_NONE][$delta] = array('fid' => $file->fid, 'display' => $file->display, 'description' => $file->description);
      }

      // Write the revision's upload field data into the field_upload tables.
      $node = (object) $revision;
      _update_7000_field_sql_storage_write('node', $node->type, $node->nid, $node->vid, 'upload', $node->file);

      // Update our progress information for the batch update.
      $sandbox['progress']++;
      $sandbox['last_vid_processed'] = $vid;
    }
  }

  // If less than limit node revisions were processed, the update process is
  // finished.
  if (count($vids) < $limit) {
    $finished = TRUE;
  }

  // If there's no max value then there's nothing to update and we're finished.
  if (empty($sandbox['max']) || isset($finished)) {
    db_drop_table('upload');
    db_drop_table('system_update_7061');
    return t('Upload module has been migrated to File module.');
  }
  else {
    // Indicate our current progress to the batch update system.
    $sandbox['#finished'] = $sandbox['progress'] / $sandbox['max'];
  }
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
