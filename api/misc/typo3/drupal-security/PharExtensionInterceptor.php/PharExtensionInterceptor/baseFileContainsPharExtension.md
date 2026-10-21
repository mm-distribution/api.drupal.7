# PharExtensionInterceptor::baseFileContainsPharExtension()

- **Type:** Method
- **File:** [`misc/typo3/drupal-security/PharExtensionInterceptor.php`](../_file.md), lines 57–77 · [local source](../../../../../../source/misc/typo3/drupal-security/PharExtensionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/drupal-security/PharExtensionInterceptor.php#L57-L77)
- **Class:** [PharExtensionInterceptor](../PharExtensionInterceptor.md)

## Signature

```php
private function baseFileContainsPharExtension($path)
```

## Documentation

```text
Determines if a path has a .phar extension or invoked execution.

@param string $path
  The path of the phar file to check.

@return bool
  TRUE if the file has a .phar extension or if the execution has been
  invoked by the phar file.
```

## Code

```php
  private function baseFileContainsPharExtension($path) {
    $baseFile = Helper::determineBaseFile($path);
    if ($baseFile === NULL) {
      return FALSE;
    }
    // If the stream wrapper is registered by invoking a phar file that does
    // not not have .phar extension then this should be allowed. For
    // example, some CLI tools recommend removing the extension.
    $backtrace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);
    // Find the last entry in the backtrace containing a 'file' key as
    // sometimes the last caller is executed outside the scope of a file. For
    // example, this occurs with shutdown functions.
    do {
      $caller = array_pop($backtrace);
    } while (empty($caller['file']) && !empty($backtrace));
    if (isset($caller['file']) && $baseFile === Helper::determineBaseFile($caller['file'])) {
      return TRUE;
    }
    $fileExtension = pathinfo($baseFile, PATHINFO_EXTENSION);
    return strtolower($fileExtension) === 'phar';
  }
```

---
_Drupal 7.103 · [misc/typo3/drupal-security/PharExtensionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/drupal-security/PharExtensionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
