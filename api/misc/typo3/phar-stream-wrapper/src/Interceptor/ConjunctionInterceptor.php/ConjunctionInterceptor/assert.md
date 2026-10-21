# ConjunctionInterceptor::assert()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php`](../_file.md), lines 38–50 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php#L38-L50)
- **Class:** [ConjunctionInterceptor](../ConjunctionInterceptor.md)

## Signature

```php
public function assert($path, $command)
```

## Documentation

```text
Executes assertions based on all contained assertions.

@param string $path
@param string $command
@return bool
@throws Exception
```

## Code

```php
    public function assert($path, $command)
    {
        if ($this->invokeAssertions($path, $command)) {
            return true;
        }
        throw new Exception(
            sprintf(
                'Assertion failed in "%s"',
                $path
            ),
            1539625084
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
