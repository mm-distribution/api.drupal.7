# FileTransfer::getSettingsForm()

- **Type:** Method
- **File:** [`includes/filetransfer/filetransfer.inc`](../_file.md), lines 331–359 · [local source](../../../../../source/includes/filetransfer/filetransfer.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc#L331-L359)
- **Class:** [FileTransfer](../FileTransfer.md)

## Signature

```php
public function getSettingsForm()
```

## Documentation

```text
Returns a form to collect connection settings credentials.

Implementing classes can either extend this form with fields collecting the
specific information they need, or override it entirely.
```

## Code

```php
  public function getSettingsForm() {
    $form['username'] = array(
      '#type' => 'textfield',
      '#title' => t('Username'),
    );
    $form['password'] = array(
      '#type' => 'password',
      '#title' => t('Password'),
      '#description' => t('Your password is not saved in the database and is only used to establish a connection.'),
    );
    $form['advanced'] = array(
      '#type' => 'fieldset',
      '#title' => t('Advanced settings'),
      '#collapsible' => TRUE,
      '#collapsed' => TRUE,
    );
    $form['advanced']['hostname'] = array(
      '#type' => 'textfield',
      '#title' => t('Host'),
      '#default_value' => 'localhost',
      '#description' => t('The connection will be created between your web server and the machine hosting the web server files. In the vast majority of cases, this will be the same machine, and "localhost" is correct.'),
    );
    $form['advanced']['port'] = array(
      '#type' => 'textfield',
      '#title' => t('Port'),
      '#default_value' => NULL,
    );
    return $form;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/filetransfer.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/filetransfer.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
