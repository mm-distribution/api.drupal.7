# DatabaseTasks_sqlite::getFormOptions()

- **Type:** Method
- **File:** [`includes/database/sqlite/install.inc`](../_file.md), lines 22–34 · [local source](../../../../../../source/includes/database/sqlite/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/install.inc#L22-L34)
- **Class:** [DatabaseTasks_sqlite](../DatabaseTasks_sqlite.md)

## Signature

```php
public function getFormOptions($database)
```

## Documentation

_No docblock in source._

## Code

```php
  public function getFormOptions($database) {
    $form = parent::getFormOptions($database);

    // Remove the options that only apply to client/server style databases.
    unset($form['username'], $form['password'], $form['advanced_options']['host'], $form['advanced_options']['port']);

    // Make the text more accurate for SQLite.
    $form['database']['#title'] = st('Database file');
    $form['database']['#description'] = st('The absolute path to the file where @drupal data will be stored. This must be writable by the web server and should exist outside of the web root.', array('@drupal' => drupal_install_profile_distribution_name()));
    $default_database = conf_path(FALSE, TRUE) . '/files/.ht.sqlite';
    $form['database']['#default_value'] = empty($database['database']) ? $default_database : $database['database'];
    return $form;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
