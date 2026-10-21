# update_fix_d7_requirements()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 478–783 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L478-L783)

## Signature

```php
function update_fix_d7_requirements()
```

## Documentation

```text
Perform Drupal 6.x to 7.x updates that are required for update.php
to function properly.

This function runs when update.php is run the first time for 7.x,
even before updates are selected or performed. It is important
that if updates are not ultimately performed that no changes are
made which make it impossible to continue using the prior version.
```

## Code

```php
function update_fix_d7_requirements() {
  global $conf;

  // Rewrite the settings.php file if necessary, see
  // update_prepare_d7_bootstrap().
  global $update_rewrite_settings, $db_url, $db_prefix;
  if (!empty($update_rewrite_settings)) {
    $databases = update_parse_db_url($db_url, $db_prefix);
    $salt = drupal_hash_base64(drupal_random_bytes(55));
    file_put_contents(conf_path() . '/settings.php', "\n" . '$databases = ' . var_export($databases, TRUE) . ";\n\$drupal_hash_salt = '$salt';", FILE_APPEND);
  }
  if (drupal_get_installed_schema_version('system') < 7000 && !variable_get('update_d7_requirements', FALSE)) {
    // Change 6.x system table field values to 7.x equivalent.
    // Change field values.
    db_change_field('system', 'schema_version', 'schema_version', array(
     'type' => 'int',
     'size' => 'small',
     'not null' => TRUE,
     'default' => -1)
    );
    db_change_field('system', 'status', 'status', array(
      'type' => 'int', 'not null' => TRUE, 'default' => 0));
    db_change_field('system', 'weight', 'weight', array(
      'type' => 'int', 'not null' => TRUE, 'default' => 0));
    db_change_field('system', 'bootstrap', 'bootstrap', array(
      'type' => 'int', 'not null' => TRUE, 'default' => 0));
    // Drop and recreate 6.x indexes.
    db_drop_index('system', 'bootstrap');
    db_add_index('system', 'bootstrap', array(
      'status', 'bootstrap', array('type', 12), 'weight', 'name'));

    db_drop_index('system' ,'modules');
    db_add_index('system', 'modules', array(array(
      'type', 12), 'status', 'weight', 'name'));

    db_drop_index('system', 'type_name');
    db_add_index('system', 'type_name', array(array('type', 12), 'name'));
    // Add 7.x indexes.
    db_add_index('system', 'system_list', array('weight', 'name'));

    // Add the cache_path table.
    if (db_table_exists('cache_path')) {
      db_drop_table('cache_path');
    }
    require_once('./modules/system/system.install');
    $schema['cache_path'] = system_schema_cache_7054();
    $schema['cache_path']['description'] = 'Cache table used for path alias lookups.';
    db_create_table('cache_path', $schema['cache_path']);

    // system_update_7042() renames columns, but these are needed to bootstrap.
    // Add empty columns for now.
    db_add_field('url_alias', 'source', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''));
    db_add_field('url_alias', 'alias', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''));

    // Add new columns to {menu_router}.
    db_add_field('menu_router', 'delivery_callback', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''));
    db_add_field('menu_router', 'context', array(
      'description' => 'Only for local tasks (tabs) - the context of a local task to control its placement.',
      'type' => 'int',
      'not null' => TRUE,
      'default' => 0,
    ));
    db_drop_index('menu_router', 'tab_parent');
    db_add_index('menu_router', 'tab_parent', array(array('tab_parent', 64), 'weight', 'title'));
    db_add_field('menu_router', 'theme_callback', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''));
    db_add_field('menu_router', 'theme_arguments', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => ''));

    // Add the role_permission table.
    $schema['role_permission'] = array(
      'fields' => array(
        'rid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'permission' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'default' => '',
      ),
    ),
    'primary key' => array('rid', 'permission'),
    'indexes' => array(
      'permission' => array('permission'),
      ),
    );
    db_create_table('role_permission', $schema['role_permission']);

    // Drops and recreates semaphore value index.
    db_drop_index('semaphore', 'value');
    db_add_index('semaphore', 'value', array('value'));

    $schema['date_format_type'] = array(
      'description' => 'Stores configured date format types.',
      'fields' => array(
        'type' => array(
          'description' => 'The date format type, e.g. medium.',
          'type' => 'varchar',
          'length' => 64,
          'not null' => TRUE,
        ),
        'title' => array(
          'description' => 'The human readable name of the format type.',
          'type' => 'varchar',
          'length' => 255,
          'not null' => TRUE,
        ),
        'locked' => array(
          'description' => 'Whether or not this is a system provided format.',
          'type' => 'int',
          'size' => 'tiny',
          'default' => 0,
          'not null' => TRUE,
        ),
      ),
      'primary key' => array('type'),
    );

    $schema['date_formats'] = array(
      'description' => 'Stores configured date formats.',
      'fields' => array(
        'dfid' => array(
          'description' => 'The date format identifier.',
          'type' => 'serial',
          'not null' => TRUE,
          'unsigned' => TRUE,
        ),
        'format' => array(
          'description' => 'The date format string.',
          'type' => 'varchar',
          'length' => 100,
          'not null' => TRUE,
        ),
        'type' => array(
          'description' => 'The date format type, e.g. medium.',
          'type' => 'varchar',
          'length' => 64,
          'not null' => TRUE,
        ),
        'locked' => array(
          'description' => 'Whether or not this format can be modified.',
          'type' => 'int',
          'size' => 'tiny',
          'default' => 0,
          'not null' => TRUE,
        ),
      ),
      'primary key' => array('dfid'),
      'unique keys' => array('formats' => array('format', 'type')),
    );

    $schema['date_format_locale'] = array(
      'description' => 'Stores configured date formats for each locale.',
      'fields' => array(
        'format' => array(
          'description' => 'The date format string.',
          'type' => 'varchar',
          'length' => 100,
          'not null' => TRUE,
        ),
        'type' => array(
          'description' => 'The date format type, e.g. medium.',
          'type' => 'varchar',
          'length' => 64,
          'not null' => TRUE,
        ),
        'language' => array(
          'description' => 'A {languages}.language for this format to be used with.',
          'type' => 'varchar',
          'length' => 12,
          'not null' => TRUE,
        ),
      ),
      'primary key' => array('type', 'language'),
    );

    db_create_table('date_format_type', $schema['date_format_type']);
    // Sites that have the Drupal 6 Date module installed already have the
    // following tables.
    if (db_table_exists('date_formats')) {
      db_rename_table('date_formats', 'd6_date_formats');
    }
    db_create_table('date_formats', $schema['date_formats']);
    if (db_table_exists('date_format_locale')) {
      db_rename_table('date_format_locale', 'd6_date_format_locale');
    }
    db_create_table('date_format_locale', $schema['date_format_locale']);

    // Add the queue table.
    $schema['queue'] = array(
      'description' => 'Stores items in queues.',
      'fields' => array(
        'item_id' => array(
          'type' => 'serial',
          'unsigned' => TRUE,
          'not null' => TRUE,
          'description' => 'Primary Key: Unique item ID.',
        ),
        'name' => array(
          'type' => 'varchar',
          'length' => 255,
          'not null' => TRUE,
          'default' => '',
          'description' => 'The queue name.',
        ),
        'data' => array(
          'type' => 'blob',
          'not null' => FALSE,
          'size' => 'big',
          'serialize' => TRUE,
          'description' => 'The arbitrary data for the item.',
        ),
        'expire' => array(
          'type' => 'int',
          'not null' => TRUE,
          'default' => 0,
          'description' => 'Timestamp when the claim lease expires on the item.',
        ),
        'created' => array(
          'type' => 'int',
          'not null' => TRUE,
          'default' => 0,
          'description' => 'Timestamp when the item was created.',
        ),
      ),
      'primary key' => array('item_id'),
      'indexes' => array(
        'name_created' => array('name', 'created'),
        'expire' => array('expire'),
      ),
    );
    // Check for queue table that may remain from D5 or D6, if found
    //drop it.
    if (db_table_exists('queue')) {
      db_drop_table('queue');
    }

    db_create_table('queue', $schema['queue']);

    // Create the sequences table.
    $schema['sequences'] = array(
      'description' => 'Stores IDs.',
      'fields' => array(
        'value' => array(
          'description' => 'The value of the sequence.',
          'type' => 'serial',
          'unsigned' => TRUE,
          'not null' => TRUE,
        ),
       ),
      'primary key' => array('value'),
    );
    // Check for sequences table that may remain from D5 or D6, if found
    //drop it.
    if (db_table_exists('sequences')) {
      db_drop_table('sequences');
    }
    db_create_table('sequences', $schema['sequences']);
    // Initialize the table with the maximum current increment of the tables
    // that will rely on it for their ids.
    $max_aid = db_query('SELECT MAX(aid) FROM {actions_aid}')->fetchField();
    $max_uid = db_query('SELECT MAX(uid) FROM {users}')->fetchField();
    $max_batch_id = db_query('SELECT MAX(bid) FROM {batch}')->fetchField();
    db_insert('sequences')->fields(array('value' => max($max_aid, $max_uid, $max_batch_id)))->execute();

    // Add column for locale context.
    if (db_table_exists('locales_source')) {
      db_add_field('locales_source', 'context', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => '', 'description' => 'The context this string applies to.'));
    }

    // Rename 'site_offline_message' variable to 'maintenance_mode_message'
    // and 'site_offline' variable to 'maintenance_mode'.
    // Old variable is removed in update for system.module, see
    // system_update_7072().
    if ($message = variable_get('site_offline_message', NULL)) {
      variable_set('maintenance_mode_message', $message);
    }
    // Old variable is removed in update for system.module, see
    // system_update_7069().
    $site_offline = variable_get('site_offline', -1);
    if ($site_offline != -1) {
      variable_set('maintenance_mode', $site_offline);
    }

    // Add ssid column and index.
    db_add_field('sessions', 'ssid', array('description' => "Secure session ID. The value is generated by Drupal's session handlers.", 'type' => 'varchar', 'length' => 128, 'not null' => TRUE, 'default' => ''));
    db_add_index('sessions', 'ssid', array('ssid'));
    // Drop existing primary key.
    db_drop_primary_key('sessions');
    // Add new primary key.
    db_add_primary_key('sessions', array('sid', 'ssid'));

    // Allow longer javascript file names.
    if (db_table_exists('languages')) {
      db_change_field('languages', 'javascript', 'javascript', array('type' => 'varchar', 'length' => 64, 'not null' => TRUE, 'default' => ''));
    }

    // Rename action description to label.
    db_change_field('actions', 'description', 'label', array('type' => 'varchar', 'length' => 255, 'not null' => TRUE, 'default' => '0'));

    variable_set('update_d7_requirements', TRUE);
  }

  update_fix_d7_install_profile();
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
