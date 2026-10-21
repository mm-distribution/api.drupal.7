# DatabaseTasks::getFormOptions()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 478–546 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L478-L546)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
public function getFormOptions($database)
```

## Documentation

```text
Return driver specific configuration options.

@param $database
 An array of driver specific configuration options.

@return
  The options form array.
```

## Code

```php
  public function getFormOptions($database) {
    $form['database'] = array(
      '#type' => 'textfield',
      '#title' => st('Database name'),
      '#default_value' => empty($database['database']) ? '' : $database['database'],
      '#size' => 45,
      '#required' => TRUE,
      '#description' => st('The name of the database your @drupal data will be stored in. It must exist on your server before @drupal can be installed.', array('@drupal' => drupal_install_profile_distribution_name())),
    );

    $form['username'] = array(
      '#type' => 'textfield',
      '#title' => st('Database username'),
      '#default_value' => empty($database['username']) ? '' : $database['username'],
      '#required' => TRUE,
      '#size' => 45,
    );

    $form['password'] = array(
      '#type' => 'password',
      '#title' => st('Database password'),
      '#default_value' => empty($database['password']) ? '' : $database['password'],
      '#required' => FALSE,
      '#size' => 45,
    );

    $form['advanced_options'] = array(
      '#type' => 'fieldset',
      '#title' => st('Advanced options'),
      '#collapsible' => TRUE,
      '#collapsed' => TRUE,
      '#description' => st("These options are only necessary for some sites. If you're not sure what you should enter here, leave the default settings or check with your hosting provider."),
      '#weight' => 10,
    );

    $profile = drupal_get_profile();
    $db_prefix = ($profile == 'standard') ? 'drupal_' : $profile . '_';
    $form['advanced_options']['db_prefix'] = array(
      '#type' => 'textfield',
      '#title' => st('Table prefix'),
      '#default_value' => '',
      '#size' => 45,
      '#description' => st('If more than one application will be sharing this database, enter a table prefix such as %prefix for your @drupal site here.', array('@drupal' => drupal_install_profile_distribution_name(), '%prefix' => $db_prefix)),
      '#weight' => 10,
    );

    $form['advanced_options']['host'] = array(
      '#type' => 'textfield',
      '#title' => st('Database host'),
      '#default_value' => empty($database['host']) ? 'localhost' : $database['host'],
      '#size' => 45,
      // Hostnames can be 255 characters long.
      '#maxlength' => 255,
      '#required' => TRUE,
      '#description' => st('If your database is located on a different server, change this.'),
    );

    $form['advanced_options']['port'] = array(
      '#type' => 'textfield',
      '#title' => st('Database port'),
      '#default_value' => empty($database['port']) ? '' : $database['port'],
      '#size' => 45,
      // The maximum port number is 65536, 5 digits.
      '#maxlength' => 5,
      '#description' => st('If your database server is listening to a non-standard port, enter its number.'),
    );

    return $form;
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
