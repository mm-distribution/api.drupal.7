# HtaccessTest::getProtectedFiles()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3315–3367 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3315-L3367)
- **Class:** [HtaccessTest](../HtaccessTest.md)
- **Module/theme:** system

## Signature

```php
protected function getProtectedFiles()
```

## Documentation

```text
Get an array of file paths for access testing.
```

## Code

```php
  protected function getProtectedFiles() {
    drupal_mkdir($path = 'public://' . $this->randomName());

    // Tests the FilesMatch directive which denies access to certain file
    // extensions.
    $file_exts_to_deny = array(
      'engine',
      'inc',
      'info',
      'install',
      'make',
      'module',
      'module~',
      'module.bak',
      'module.orig',
      'module.save',
      'module.swo',
      'module.swp',
      'php~',
      'php.bak',
      'php.orig',
      'php.save',
      'php.swo',
      'php.swp',
      'profile',
      'po',
      'sh',
      'sql',
      'test',
      'theme',
      'tpl.php',
      'xtmpl',
    );

    foreach ($file_exts_to_deny as $file_ext) {
      $file_paths["$path/access_test.$file_ext"] = 403;
    }

    // Test extensions that should be permitted.
    $file_exts_to_allow = array(
      'php-info.txt',
    );

    foreach ($file_exts_to_allow as $file_ext) {
      $file_paths["$path/access_test.$file_ext"] = 200;
    }

    // Ensure web server configuration files cannot be accessed.
    $file_paths["$path/.htaccess"] = 403;
    $file_paths["$path/web.config"] = 403;

    return $file_paths;
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
