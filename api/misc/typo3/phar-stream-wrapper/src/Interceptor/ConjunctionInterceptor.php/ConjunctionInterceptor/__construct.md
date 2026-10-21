# ConjunctionInterceptor::__construct()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php`](../_file.md), lines 24–28 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php#L24-L28)
- **Class:** [ConjunctionInterceptor](../ConjunctionInterceptor.md)

## Signature

```php
public function __construct(array $assertions)
```

## Documentation

_No docblock in source._

## Code

```php
    public function __construct(array $assertions)
    {
        $this->assertAssertions($assertions);
        $this->assertions = $assertions;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/ConjunctionInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
