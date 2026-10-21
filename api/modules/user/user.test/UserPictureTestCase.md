# UserPictureTestCase

- **Type:** Class
- **File:** [`modules/user/user.test`](_file.md), lines 1362–1675 · [local source](../../../../source/modules/user/user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test#L1362-L1675)
- **Module/theme:** user

## Signature

```php
class UserPictureTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $user

```php
protected $user;
```

### $_directory_test

```php
protected $_directory_test;
```

## Methods (derived index)

- [getInfo()](UserPictureTestCase/getInfo.md)
- [setUp()](UserPictureTestCase/setUp.md)
- [testNoPicture()](UserPictureTestCase/testNoPicture.md)
- [testWithGDinvalidDimension()](UserPictureTestCase/testWithGDinvalidDimension.md) — Do the test: GD Toolkit is installed Picture has invalid dimension
- [testWithGDinvalidSize()](UserPictureTestCase/testWithGDinvalidSize.md) — Do the test: GD Toolkit is installed Picture has invalid size
- [testWithoutGDinvalidDimension()](UserPictureTestCase/testWithoutGDinvalidDimension.md) — Do the test: GD Toolkit is not installed Picture has invalid size
- [testWithoutGDinvalidSize()](UserPictureTestCase/testWithoutGDinvalidSize.md) — Do the test: GD Toolkit is not installed Picture has invalid size
- [testPictureIsValid()](UserPictureTestCase/testPictureIsValid.md) — Do the test: Picture is valid (proper size and dimension)
- [testExternalPicture()](UserPictureTestCase/testExternalPicture.md) — Test HTTP schema working with user pictures.
- [testDeletePicture()](UserPictureTestCase/testDeletePicture.md) — Tests deletion of user pictures.
- [saveUserPicture()](UserPictureTestCase/saveUserPicture.md)
- [testUserPictureAdminFormValidation()](UserPictureTestCase/testUserPictureAdminFormValidation.md) — Tests the admin form validates user picture settings.

---
_Drupal 7.103 · [modules/user/user.test](https://github.com/drupal/drupal/blob/7.103/modules/user/user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
