# DrupalDummyRemoteStreamWrapper

- **Type:** Class
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 465–469 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L465-L469)
- **Module/theme:** batch_test

## Signature

```php
class DrupalDummyRemoteStreamWrapper extends DrupalPublicStreamWrapper
```

## Documentation

```text
Helper class for testing the stream wrapper registry.

Dummy remote stream wrapper implementation (dummy-remote://).

Basically just the public scheme but not returning a local file for realpath.
```

## Methods (derived index)

- [realpath()](DrupalDummyRemoteStreamWrapper/realpath.md)

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
