# Manifest::deserializeMetaData()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php`](../_file.md), lines 158–175 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php#L158-L175)
- **Class:** [Manifest](../Manifest.md)

## Signature

```php
public function deserializeMetaData()
```

## Documentation

```text
@return mixed|null
```

## Code

```php
    public function deserializeMetaData()
    {
        if (empty($this->metaData)) {
            return null;
        }

        $result = Unserialize::unserialize($this->metaData, array('allowed_classes' => false));

        $serialized = json_encode($result);
        if (strpos($serialized, '__PHP_Incomplete_Class_Name') !== false) {
            throw new DeserializationException(
                'Meta-data contains serialized object',
                1539623382
            );
        }

        return $result;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php) · Licensed GPL-2.0-or-later (see LICENSE)._
