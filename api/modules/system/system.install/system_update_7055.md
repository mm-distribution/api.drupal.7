# system_update_7055()

- **Type:** Function
- **File:** [`modules/system/system.install`](_file.md), lines 2629–2705 · [local source](../../../../source/modules/system/system.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install#L2629-L2705)
- **Module/theme:** system
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function system_update_7055()
```

## Documentation

```text
Converts fields that store serialized variables from text to blob.
```

## Code

```php
function system_update_7055() {
  $spec = array(
    'description' => 'The value of the variable.',
    'type' => 'blob',
    'not null' => TRUE,
    'size' => 'big',
    'translatable' => TRUE,
  );
  db_change_field('variable', 'value', 'value', $spec);

  $spec = array(
    'description' => 'Parameters to be passed to the callback function.',
    'type' => 'blob',
    'not null' => TRUE,
    'size' => 'big',
  );
  db_change_field('actions', 'parameters', 'parameters', $spec);

  $spec = array(
    'description' => 'A serialized array containing the processing data for the batch.',
    'type' => 'blob',
    'not null' => FALSE,
    'size' => 'big',
  );
  db_change_field('batch', 'batch', 'batch', $spec);

  $spec = array(
    'description' => 'A serialized array of function names (like node_load) to be called to load an object corresponding to a part of the current path.',
    'type' => 'blob',
    'not null' => TRUE,
  );
  db_change_field('menu_router', 'load_functions', 'load_functions', $spec);

  $spec = array(
    'description' => 'A serialized array of function names (like user_uid_optional_to_arg) to be called to replace a part of the router path with another string.',
    'type' => 'blob',
    'not null' => TRUE,
  );
  db_change_field('menu_router', 'to_arg_functions', 'to_arg_functions', $spec);

  $spec = array(
    'description' => 'A serialized array of arguments for the access callback.',
    'type' => 'blob',
    'not null' => FALSE,
  );
  db_change_field('menu_router', 'access_arguments', 'access_arguments', $spec);

  $spec = array(
    'description' => 'A serialized array of arguments for the page callback.',
    'type' => 'blob',
    'not null' => FALSE,
  );
  db_change_field('menu_router', 'page_arguments', 'page_arguments', $spec);

  $spec = array(
    'description' => 'A serialized array of options to be passed to the url() or l() function, such as a query string or HTML attributes.',
    'type' => 'blob',
    'not null' => FALSE,
    'translatable' => TRUE,
  );
  db_change_field('menu_links', 'options', 'options', $spec);

  $spec = array(
    'description' => 'The serialized contents of $_SESSION, an array of name/value pairs that persists across page requests by this session ID. Drupal loads $_SESSION from here at the start of each request and saves it at the end.',
    'type' => 'blob',
    'not null' => FALSE,
    'size' => 'big',
  );
  db_change_field('sessions', 'session', 'session', $spec);

  $spec = array(
    'description' => "A serialized array containing information from the module's .info file; keys can include name, description, package, version, core, dependencies, and php.",
    'type' => 'blob',
    'not null' => FALSE,
  );
  db_change_field('system', 'info', 'info', $spec);
}
```

---
_Drupal 7.103 · [modules/system/system.install](https://github.com/drupal/drupal/blob/7.103/modules/system/system.install) · Licensed GPL-2.0-or-later (see LICENSE)._
