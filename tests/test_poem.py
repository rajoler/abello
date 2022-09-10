from abello.poems import main


def test_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out.count('\n') >= 2

def test_poems():
    from abello.poems import poems
    assert isinstance(poems, list)
    assert len(poems) > 0
    for poem in poems:
        assert isinstance(poem, list)
        assert len(poem) == 2
        assert isinstance(poem[0], str)
        assert isinstance(poem[1], str)
