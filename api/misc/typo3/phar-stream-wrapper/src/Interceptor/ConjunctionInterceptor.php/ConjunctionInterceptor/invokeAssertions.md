# ConjunctionInterceptor::invokeAssertions()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php`](../_file.md), lines 75–87 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php#L75-L87)
- **Class:** [ConjunctionInterceptor](../ConjunctionInterceptor.md)

## Signature

```php
private function invokeAssertions($path, $command)
```

## Documentation

```text
@param string $path
@param string $command
@return bool
```

## Code

```php
    private function invokeAssertions($path, $command)
    {
        try {
            foreach ($this->assertions as $assertion) {
                if (!$assertion->assert($path, $command)) {
                    return false;
                }
            }
        } catch (Exception $exception) {
            return false;
        }
        return true;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
