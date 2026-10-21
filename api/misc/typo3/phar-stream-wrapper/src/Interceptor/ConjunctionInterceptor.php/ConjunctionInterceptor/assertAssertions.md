# ConjunctionInterceptor::assertAssertions()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php`](../_file.md), lines 55–68 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php#L55-L68)
- **Class:** [ConjunctionInterceptor](../ConjunctionInterceptor.md)

## Signature

```php
private function assertAssertions(array $assertions)
```

## Documentation

```text
@param Assertable[] $assertions
```

## Code

```php
    private function assertAssertions(array $assertions)
    {
        foreach ($assertions as $assertion) {
            if (!$assertion instanceof Assertable) {
                throw new \InvalidArgumentException(
                    sprintf(
                        'Instance %s must implement Assertable',
                        get_class($assertion)
                    ),
                    1539624719
                );
            }
        }
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
