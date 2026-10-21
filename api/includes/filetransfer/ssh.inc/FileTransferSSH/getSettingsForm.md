# FileTransferSSH::getSettingsForm()

- **Type:** Method
- **File:** [`includes/filetransfer/ssh.inc`](../_file.md), lines 105–109 · [local source](../../../../../source/includes/filetransfer/ssh.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc#L105-L109)
- **Class:** [FileTransferSSH](../FileTransferSSH.md)

## Signature

```php
public function getSettingsForm()
```

## Documentation

```text
Returns the form to configure the FileTransfer class for SSH.
```

## Code

```php
  public function getSettingsForm() {
    $form = parent::getSettingsForm();
    $form['advanced']['port']['#default_value'] = 22;
    return $form;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ssh.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ssh.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
