# PharMetaDataInterceptor::assert()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php`](../_file.md), lines 35–47 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php#L35-L47)
- **Class:** [PharMetaDataInterceptor](../PharMetaDataInterceptor.md)

## Signature

```php
public function assert($path, $command)
```

## Documentation

```text
Determines whether the according Phar archive contains
(potential insecure) serialized objects.

@param string $path
@param string $command
@return bool
@throws Exception
```

## Code

```php
    public function assert($path, $command)
    {
        if ($this->baseFileDoesNotHaveMetaDataIssues($path)) {
            return true;
        }
        throw new Exception(
            sprintf(
                'Problematic meta-data in "%s"',
                $path
            ),
            1539632368
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
