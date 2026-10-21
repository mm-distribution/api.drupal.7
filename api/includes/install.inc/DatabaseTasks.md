# DatabaseTasks

- **Type:** Class
- **File:** [`includes/install.inc`](_file.md), lines 290–576 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L290-L576)

## Signature

```php
abstract class DatabaseTasks
```

## Documentation

```text
Database installer structure.

Defines basic Drupal requirements for databases.
```

## Properties

### $tasks

```php
protected $tasks = array(
    array(
      'function'    => 'checkEngineVersion',
      'arguments'   => array(),
    ),
    array(
      'arguments'   => array(
        'CREATE TABLE {drupal_install_test} (id int NULL)',
        'Drupal can use CREATE TABLE database commands.',
        'Failed to <strong>CREATE</strong> a test table on your database server with the command %query. The server reports the following message: %error.<p>Are you sure the configured username has the necessary permissions to create tables in the database?</p>',
        TRUE,
      ),
    ),
    array(
      'arguments'   => array(
        'INSERT INTO {drupal_install_test} (id) VALUES (1)',
        'Drupal can use INSERT database commands.',
        'Failed to <strong>INSERT</strong> a value into a test table on your database server. We tried inserting a value with the command %query and the server reported the following error: %error.',
      ),
    ),
    array(
      'arguments'   => array(
        'UPDATE {drupal_install_test} SET id = 2',
        'Drupal can use UPDATE database commands.',
        'Failed to <strong>UPDATE</strong> a value in a test table on your database server. We tried updating a value with the command %query and the server reported the following error: %error.',
      ),
    ),
    array(
      'arguments'   => array(
        'DELETE FROM {drupal_install_test}',
        'Drupal can use DELETE database commands.',
        'Failed to <strong>DELETE</strong> a value from a test table on your database server. We tried deleting a value with the command %query and the server reported the following error: %error.',
      ),
    ),
    array(
      'arguments'   => array(
        'DROP TABLE {drupal_install_test}',
        'Drupal can use DROP TABLE database commands.',
        'Failed to <strong>DROP</strong> a test table from your database server. We tried dropping a table with the command %query and the server reported the following error %error.',
      ),
    ),
  );
```

```text
Structure that describes each task to run.

@var array

Each value of the tasks array is an associative array defining the function
to call (optional) and any arguments to be passed to the function.
```

### $results

```php
protected $results = array();
```

```text
Results from tasks.

@var array
```

## Methods (derived index)

- [hasPdoDriver()](DatabaseTasks/hasPdoDriver.md) — Ensure the PDO driver is supported by the version of PHP in use.
- [fail()](DatabaseTasks/fail.md) — Assert test as failed.
- [pass()](DatabaseTasks/pass.md) — Assert test as a pass.
- [installable()](DatabaseTasks/installable.md) — Check whether Drupal is installable on the database.
- [name()](DatabaseTasks/name.md) — Return the human-readable name of the driver.
- [minimumVersion()](DatabaseTasks/minimumVersion.md) — Return the minimum required version of the engine.
- [runTasks()](DatabaseTasks/runTasks.md) — Run database tasks and tests to see if Drupal can run on the database.
- [connect()](DatabaseTasks/connect.md) — Check if we can connect to the database.
- [runTestQuery()](DatabaseTasks/runTestQuery.md) — Run SQL tests to ensure the database can execute commands with the current user.
- [checkEngineVersion()](DatabaseTasks/checkEngineVersion.md) — Check the engine version.
- [getFormOptions()](DatabaseTasks/getFormOptions.md) — Return driver specific configuration options.
- [validateDatabaseSettings()](DatabaseTasks/validateDatabaseSettings.md) — Validates driver specific configuration settings.

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
