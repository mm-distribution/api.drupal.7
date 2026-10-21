# PharExtensionInterceptor::assert()

- **Type:** Method
- **File:** [`misc/typo3/drupal-security/PharExtensionInterceptor.php`](../_file.md), lines 34–45 · [local source](../../../../../../source/misc/typo3/drupal-security/PharExtensionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/drupal-security/PharExtensionInterceptor.php#L34-L45)
- **Class:** [PharExtensionInterceptor](../PharExtensionInterceptor.md)

## Signature

```php
public function assert($path, $command)
```

## Documentation

```text
Determines whether phar file is allowed to execute.

The phar file is allowed to execute if:
- the base file name has a ".phar" suffix.
- it is the CLI tool that has invoked the interceptor.

@param string $path
  The path of the phar file to check.
@param string $command
  The command being carried out.

@return bool
  TRUE if the phar file is allowed to execute.

@throws Exception
  Thrown when the file is not allowed to execute.
```

## Code

```php
  public function assert($path, $command) {
    if ($this->baseFileContainsPharExtension($path)) {
      return TRUE;
    }
    throw new Exception(
      sprintf(
        'Unexpected file extension in "%s"',
        $path
      ),
      1535198703
    );
  }
```

---
_Drupal 7.103 · [misc/typo3/drupal-security/PharExtensionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/drupal-security/PharExtensionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
