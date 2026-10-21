# FileScanDirectory::testNoMask()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1983–2001 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1983-L2001)
- **Class:** [FileScanDirectory](../FileScanDirectory.md)
- **Module/theme:** file_module_test

## Signature

```php
public function testNoMask()
```

## Documentation

```text
Tests file_scan_directory() obeys 'file_scan_ignore_directories' setting.
If nomask is not passed as argument, it should use the default settings.
If nomask is passed as argument, it should obey this rule.
```

## Code

```php
  public function testNoMask() {
    $files = file_scan_directory($this->path, '/\.txt$/');
    $this->assertEqual(3, count($files), '3 text files found when not ignoring directories.');

    global $conf;
    $conf['file_scan_ignore_directories'] = array('frontend_framework');

    $files = file_scan_directory($this->path, '/\.txt$/');
    $this->assertEqual(1, count($files), '1 text files found when ignoring directories called "frontend_framework".');

    // Make that directories specified by default still work when a new nomask is provided.
    $files = file_scan_directory($this->path, '/\.txt$/', array('nomask' => '/^c.txt/'));
    $this->assertEqual(2, count($files), '2 text files found when an "nomask" option is passed in.');

    // Ensure that the directories in file_scan_ignore_directories are escaped using preg_quote.
    $conf['file_scan_ignore_directories'] = array('frontend.*');
    $files = file_scan_directory($this->path, '/\.txt$/');
    $this->assertEqual(3, count($files), '2 text files found when ignoring a directory that is not there.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
