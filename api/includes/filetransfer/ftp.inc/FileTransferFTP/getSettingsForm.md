# FileTransferFTP::getSettingsForm()

- **Type:** Method
- **File:** [`includes/filetransfer/ftp.inc`](../_file.md), lines 44–48 · [local source](../../../../../source/includes/filetransfer/ftp.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc#L44-L48)
- **Class:** [FileTransferFTP](../FileTransferFTP.md)

## Signature

```php
public function getSettingsForm()
```

## Documentation

```text
Returns the form to configure the FileTransfer class for FTP.
```

## Code

```php
  public function getSettingsForm() {
    $form = parent::getSettingsForm();
    $form['advanced']['port']['#default_value'] = 21;
    return $form;
  }
```

---
_Drupal 7.103 · [includes/filetransfer/ftp.inc](https://github.com/drupal/drupal/blob/7.103/includes/filetransfer/ftp.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
