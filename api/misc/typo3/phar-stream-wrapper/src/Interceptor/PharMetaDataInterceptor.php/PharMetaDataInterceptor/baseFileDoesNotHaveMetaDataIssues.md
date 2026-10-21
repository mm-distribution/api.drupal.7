# PharMetaDataInterceptor::baseFileDoesNotHaveMetaDataIssues()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php`](../_file.md), lines 53–72 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php#L53-L72)
- **Class:** [PharMetaDataInterceptor](../PharMetaDataInterceptor.md)

## Signature

```php
private function baseFileDoesNotHaveMetaDataIssues($path)
```

## Documentation

```text
@param string $path
@return bool
```

## Code

```php
    private function baseFileDoesNotHaveMetaDataIssues($path)
    {
        $invocation = Manager::instance()->resolve($path);
        if ($invocation === null) {
            return false;
        }
        // directly return in case invocation was checked before
        if ($invocation->getVariable(__CLASS__) === true) {
            return true;
        }
        // otherwise analyze meta-data
        try {
            $reader = new Reader($invocation->getBaseName());
            $reader->resolveContainer()->getManifest()->deserializeMetaData();
            $invocation->setVariable(__CLASS__, true);
        } catch (DeserializationException $exception) {
            return false;
        }
        return true;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Interceptor/PharMetaDataInterceptor.php) · Licensed GPL-2.0-or-later (see LICENSE)._
