from abello.poems import main

def test_main(capsys):
    main()
    out, err = capsys.readouterr()
    assert out.count('\n') >= 2
    
    
