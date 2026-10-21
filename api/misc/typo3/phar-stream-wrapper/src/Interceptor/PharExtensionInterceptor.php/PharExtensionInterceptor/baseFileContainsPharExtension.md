# PharExtensionInterceptor::baseFileContainsPharExtension()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php`](../_file.md), lines 46–54 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php#L46-L54)
- **Class:** [PharExtensionInterceptor](../PharExtensionInterceptor.md)

## Signature

```php
private function baseFileContainsPharExtension($path)
```

## Documentation

```text
@param string $path
@return bool
```

## Code

```php
    private function baseFileContainsPharExtension($path)
    {
        $invocation = Manager::instance()->resolve($path);
        if ($invocation === null) {
            return false;
        }
        $fileExtension = pathinfo($invocation->getBaseName(), PATHINFO_EXTENSION);
        return strtolower($fileExtension) === 'phar';
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
