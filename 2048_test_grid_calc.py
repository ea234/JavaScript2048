# 
# Test of the Algorithm
#
# startGridCalc ######################################################################
# 
#           [2, 0, 2, 2, 4, 0, 2, 2]
# 
# S 0  0  1  2 0 [2, 0, 2, 2, 4, 0, 2, 2]
# E 1  0  2  2 0 [2, 0, 2, 2, 4, 0, 2, 2]
# 
# S 1  0  2  2 2 [2, 0, 2, 2, 4, 0, 2, 2]
# E 2  1  3  2 2 [4, 0, 0, 2, 4, 0, 2, 2]
# 
# S 2  1  3  0 2 [4, 0, 0, 2, 4, 0, 2, 2]
# E 3  1  4  0 2 [4, 2, 0, 0, 4, 0, 2, 2]
# 
# S 3  1  4  2 4 [4, 2, 0, 0, 4, 0, 2, 2]
# E 4  2  5  0 4 [4, 2, 4, 0, 0, 0, 2, 2]
# 
# S 4  2  5  4 0 [4, 2, 4, 0, 0, 0, 2, 2]
# E 5  2  6  4 0 [4, 2, 4, 0, 0, 0, 2, 2]
# 
# S 5  2  6  4 2 [4, 2, 4, 0, 0, 0, 2, 2]
# E 6  3  7  0 2 [4, 2, 4, 2, 0, 0, 0, 2]
# 
# S 6  3  7  2 2 [4, 2, 4, 2, 0, 0, 0, 2]
# E 7  4  8  2 2 [4, 2, 4, 4, 0, 0, 0, 0]
# 
# 7  4  8   [4, 2, 4, 4, 0, 0, 0, 0]
# 
#           [4, 2, 4, 4, 0, 0, 0, 0]
# 
# 
# startGridCalc ######################################################################
# 
#           [2, 0, 2, 2, 4, 0, 2, 2]
# 
# S 0  7  6  2 2 [2, 0, 2, 2, 4, 0, 2, 2]
# E 1  6  5  2 2 [2, 0, 2, 2, 4, 0, 0, 4]
# 
# S 1  6  5  0 0 [2, 0, 2, 2, 4, 0, 0, 4]
# E 2  6  4  0 0 [2, 0, 2, 2, 4, 0, 0, 4]
# 
# S 2  6  4  0 4 [2, 0, 2, 2, 4, 0, 0, 4]
# E 3  6  3  0 4 [2, 0, 2, 2, 0, 0, 4, 4]
# 
# S 3  6  3  4 2 [2, 0, 2, 2, 0, 0, 4, 4]
# E 4  5  2  0 2 [2, 0, 2, 0, 0, 2, 4, 4]
# 
# S 4  5  2  2 2 [2, 0, 2, 0, 0, 2, 4, 4]
# E 5  4  1  2 2 [2, 0, 0, 0, 0, 4, 4, 4]
# 
# S 5  4  1  0 0 [2, 0, 0, 0, 0, 4, 4, 4]
# E 6  4  0  0 0 [2, 0, 0, 0, 0, 4, 4, 4]
# 
# S 6  4  0  0 2 [2, 0, 0, 0, 0, 4, 4, 4]
# E 7  4  -1  0 2 [0, 0, 0, 0, 2, 4, 4, 4]
# 
# 7  4  -1   [0, 0, 0, 0, 2, 4, 4, 4]
# 
#           [0, 0, 0, 0, 2, 4, 4, 4]
# 
# 
# startGridCalc ######################################################################
# 
#           [1, 2, 3, 4, 5]
# 
# S 0  0  1  1 2 [1, 2, 3, 4, 5]
# E 1  1  2  2 2 [1, 2, 3, 4, 5]
# 
# S 1  1  2  2 3 [1, 2, 3, 4, 5]
# E 2  2  3  3 3 [1, 2, 3, 4, 5]
# 
# S 2  2  3  3 4 [1, 2, 3, 4, 5]
# E 3  3  4  4 4 [1, 2, 3, 4, 5]
# 
# S 3  3  4  4 5 [1, 2, 3, 4, 5]
# E 4  4  5  5 5 [1, 2, 3, 4, 5]
# 
# 4  4  5   [1, 2, 3, 4, 5]
# 
#           [1, 2, 3, 4, 5]
# 
# 
# startGridCalc ######################################################################
# 
#           [8, 8, 0, 4]
#           [16, 4, 0, 0]
# 
# 
# startGridCalc ######################################################################
# 
#           [8, 8, 0, 4]
#           [0, 0, 16, 4]
# 
# 
# startGridCalc ######################################################################
# 
#           [2, 4, 2, 4]
#           [2, 4, 2, 4]
# 
# 
# startGridCalc ######################################################################
# 
#           [2, 4, 2, 4]
#           [2, 4, 2, 4]




def startGridCalc( pGrid, pIncWert, pKnzDebugZwischenwerte ):

    print ( "" )
    print ( "startGridCalc ######################################################################")
    print ( "" )
    print ( f"          {pGrid}")
    
    if ( pKnzDebugZwischenwerte ):
        print ( "" )

    anzahl_spalten = len( pGrid )
   
    inc_wert = pIncWert

    if ( pIncWert < 1 ):
        
        inc_wert = -1

        index_abbruch = -1

        akt_summe_index = anzahl_spalten - 1
        
        akt_position_index = akt_summe_index - 1

    else:

        inc_wert = 1

        index_abbruch = anzahl_spalten

        akt_summe_index = 0
        
        akt_position_index = akt_summe_index + 1

    akt_summe_wert = 0
    akt_position_wert = 0

    zaehler_spalte = 0

    while ( ( zaehler_spalte <= anzahl_spalten ) and ( akt_position_index != index_abbruch ) ):
        #
        # Werte an den Positionen in lokale Variablen speichern.
        # (nicht zwingend notwendig, macht den Algorithmus aber einfacher zu lesen)
        #
        akt_summe_wert = pGrid[ akt_summe_index ]
        akt_position_wert = pGrid[ akt_position_index ]

        if ( pKnzDebugZwischenwerte ):

            print ( f"S {zaehler_spalte}  {akt_summe_index}  {akt_position_index}  {akt_summe_wert} {akt_position_wert} {pGrid}")
     
        if ( akt_position_wert > 0 ):
            
            if ( akt_position_wert == akt_summe_wert ):
            
                pGrid[ akt_summe_index ] = akt_summe_wert + akt_position_wert
                
                pGrid[ akt_position_index ] = 0
                
                akt_summe_index += inc_wert
                   
            elif ( akt_summe_wert == 0 ):
                
                pGrid[ akt_summe_index ] = akt_position_wert
                
                pGrid[ akt_position_index ] = 0
                   
            elif ( akt_summe_wert > 0 ):
     
                akt_summe_index += inc_wert
            
                while ( ( pGrid[ akt_summe_index ] > 0 ) and ( akt_summe_index != akt_position_index ) ):
                
                    akt_summe_index += inc_wert
                
                akt_summe_wert = pGrid[ akt_summe_index ]
                
                if ( akt_summe_index != akt_position_index ):
                
                    if ( akt_position_wert == akt_summe_wert ):
                    
                        pGrid[ akt_summe_index ] = akt_summe_wert + akt_position_wert
                        
                        pGrid[ akt_position_index ] = 0
                        
                        akt_summe_index += inc_wert
                        
                    elif ( akt_summe_wert == 0 ):
                        
                        pGrid[ akt_summe_index ] = akt_position_wert
                        
                        pGrid[ akt_position_index ] = 0
                    

        akt_position_index += inc_wert

        zaehler_spalte += 1
        
        if ( pKnzDebugZwischenwerte ):
            print ( f"E {zaehler_spalte}  {akt_summe_index}  {akt_position_index}  {akt_summe_wert} {akt_position_wert} {pGrid}")
            print ( "" )
        
    if ( pKnzDebugZwischenwerte ):
        print ( f"{zaehler_spalte}  {akt_summe_index}  {akt_position_index}   {pGrid}")
        print ( "" )
        
    print ( f"          {pGrid}")
    print ( "" )



grid_start = [ 2,0,2,2,4,0,2,2 ]


startGridCalc( grid_start[:], 1, True )

startGridCalc( grid_start[:], -1, True )


grid_start = [ 1,2,3,4,5 ]

startGridCalc( grid_start[:], 1, True )


grid_start = [ 8, 8, 0, 4 ]

startGridCalc( grid_start[:], 1, False )

startGridCalc( grid_start[:], -1, False )


grid_start = [ 2,4,2,4 ]

startGridCalc( grid_start[:], 1, False )

startGridCalc( grid_start[:], -1, False )
