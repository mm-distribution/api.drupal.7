# node_update_7006()

- **Type:** Function
- **File:** [`modules/node/node.install`](_file.md), lines 607–787 · [local source](../../../../source/modules/node/node.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install#L607-L787)
- **Module/theme:** node
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function node_update_7006(&$sandbox)
```

## Documentation

```text
Convert body and teaser from node properties to fields, and migrate status/comment/promote and sticky columns to the {node_revision} table.
```

## Code

```php
function node_update_7006(&$sandbox) {
  $sandbox['#finished'] = 0;

  // Get node type info for every invocation.
  node_type_cache_reset();

  if (!isset($sandbox['total'])) {
    // Initial invocation.

    // First, create the body field.
    $body_field = array(
      'field_name' => 'body',
      'type' => 'text_with_summary',
      'module' => 'text',
      'cardinality' => 1,
      'entity_types' => array('node'),
      'translatable' => TRUE,
    );
    _update_7000_field_create_field($body_field);

    $default_trim_length = variable_get('teaser_length', 600);

    // Get node type info, specifically the body field settings.
    $node_types = _update_7000_node_get_types();

    // Add body field instances for existing node types.
    foreach ($node_types as $node_type) {
      if ($node_type->has_body) {
        $trim_length = variable_get('teaser_length_' . $node_type->type, $default_trim_length);

        $instance = array(
          'entity_type' => 'node',
          'bundle' => $node_type->type,
          'label' => $node_type->body_label,
          'description' => isset($node_type->description) ? $node_type->description : '',
          'required' => (isset($node_type->min_word_count) && $node_type->min_word_count > 0) ? 1 : 0,
          'widget' => array(
            'type' => 'text_textarea_with_summary',
            'settings' => array(
              'rows' => 20,
              'summary_rows' => 5,
            ),
            'weight' => -4,
            'module' => 'text',
          ),
          'settings' => array('display_summary' => TRUE),
          'display' => array(
            'default' => array(
              'label' => 'hidden',
              'type' => 'text_default',
            ),
            'teaser' => array(
              'label' => 'hidden',
              'type' => 'text_summary_or_trimmed',
              'trim_length' => $trim_length,
            ),
          ),
        );
        _update_7000_field_create_instance($body_field, $instance);
        variable_del('teaser_length_' . $node_type->type);
      }
      // Leave 'teaser_length' variable for aggregator module upgrade.

      $sandbox['node_types_info'][$node_type->type] = array(
        'has_body' => $node_type->has_body,
      );
    }

    // Used below when updating the stored text format of each node body.
    $sandbox['existing_text_formats'] = db_query("SELECT format FROM {filter_format}")->fetchCol();

    // Initialize state for future calls.
    $sandbox['last'] = 0;
    $sandbox['count'] = 0;

    $query = db_select('node', 'n');
    $query->join('node_revision', 'nr', 'n.nid = nr.nid');
    $sandbox['total'] = $query->countQuery()->execute()->fetchField();

    $sandbox['body_field_id'] = $body_field['id'];
  }
  else {
    // Subsequent invocations.

    $found = FALSE;
    if ($sandbox['total']) {
      // Operate on every revision of every node (whee!), in batches.
      $batch_size = 200;
      $query = db_select('node_revision', 'nr');
      $query->innerJoin('node', 'n', 'n.nid = nr.nid');
      $query
        ->fields('nr', array('nid', 'vid', 'body', 'teaser', 'format'))
        ->fields('n', array('type', 'status', 'comment', 'promote', 'sticky', 'language'))
        ->condition('nr.vid', $sandbox['last'], '>')
        ->orderBy('nr.vid', 'ASC')
        ->range(0, $batch_size);
      $revisions = $query->execute();

      // Load each revision of each node, set up 'body'
      // appropriately, and save the node's field data.  Note that
      // node_load() will not return the body or teaser values from
      // {node_revision} because those columns have been removed from the
      // schema structure in memory (but not yet from the database),
      // so we get the values from the explicit query of the table
      // instead.
      foreach ($revisions as $revision) {
        $found = TRUE;

        if ($sandbox['node_types_info'][$revision->type]['has_body']) {
          $node = (object) array(
            'nid' => $revision->nid,
            'vid' => $revision->vid,
            'type' => $revision->type,
          );
          // After node_update_7009() we will always have LANGUAGE_NONE as
          // language neutral language code, but here we still have empty
          // strings.
          $langcode = empty($revision->language) ? LANGUAGE_NONE : $revision->language;
          if (!empty($revision->teaser) && $revision->teaser != text_summary($revision->body)) {
            $node->body[$langcode][0]['summary'] = $revision->teaser;
          }
          // Do this after text_summary() above.
          $break = '<!--break-->';
          if (substr($revision->body, 0, strlen($break)) == $break) {
            $revision->body = substr($revision->body, strlen($break));
          }
          $node->body[$langcode][0]['value'] = $revision->body;
          // Update the revision's text format for the changes to the Drupal 7
          // filter system. This uses the same kind of logic that occurs, for
          // example, in user_update_7010(), but we do this here rather than
          // via a separate set of database queries, since we are already
          // migrating the data.
          if (empty($revision->body) && empty($revision->format)) {
            $node->body[$langcode][0]['format'] = NULL;
          }
          elseif (!in_array($revision->format, $sandbox['existing_text_formats'])) {
            $node->body[$langcode][0]['format'] = variable_get('filter_default_format', 1);
          }
          else {
            $node->body[$langcode][0]['format'] = $revision->format;
          }
          // This is a core update and no contrib modules are enabled yet, so
          // we can assume default field storage for a faster update.
          _update_7000_field_sql_storage_write('node', $node->type, $node->nid, $node->vid, 'body', $node->body);
        }

        // Migrate the status columns to the {node_revision} table.
        db_update('node_revision')
          ->fields(array(
            'status' => $revision->status,
            'comment' => $revision->comment,
            'promote' => $revision->promote,
            'sticky' => $revision->sticky,
          ))
          ->condition('vid', $revision->vid)
          ->execute();

        $sandbox['last'] = $revision->vid;
        $sandbox['count'] += 1;
      }

      $sandbox['#finished'] = min(0.99, $sandbox['count'] / $sandbox['total']);
    }

    if (!$found) {
      // All nodes are processed.

      // Remove the now-obsolete body info from node_revision.
      db_drop_field('node_revision', 'body');
      db_drop_field('node_revision', 'teaser');
      db_drop_field('node_revision', 'format');

      // Remove node_type properties related to the former 'body'.
      db_drop_field('node_type', 'has_body');
      db_drop_field('node_type', 'body_label');

      // We're done.
      $sandbox['#finished'] = 1;
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/node.install](https://github.com/drupal/drupal/blob/7.103/modules/node/node.install) · Licensed GPL-2.0-or-later (see LICENSE)._
