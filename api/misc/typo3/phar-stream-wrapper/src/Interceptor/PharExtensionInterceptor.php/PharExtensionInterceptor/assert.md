# PharExtensionInterceptor::assert()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php`](../_file.md), lines 28–40 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php#L28-L40)
- **Class:** [PharExtensionInterceptor](../PharExtensionInterceptor.md)

## Signature

```php
public function assert($path, $command)
```

## Documentation

```text
Determines whether the base file name has a ".phar" suffix.

@param string $path
@param string $command
@return bool
@throws Exception
```

## Code

```php
    public function assert($path, $command)
    {
        if ($this->baseFileContainsPharExtension($path)) {
            return true;
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
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharExtensionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
