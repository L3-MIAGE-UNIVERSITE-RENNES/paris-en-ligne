package com.trodieng.parisportif.model;

import javax.persistence.*;

import org.openxava.annotations.*;
import org.openxava.model.*;

import lombok.*;
@Entity @Getter @Setter
public class Pari extends Identifiable  {
	@Column
	private int montant;
	@Column
	private String resultat;
	@ManyToOne( 
	        fetch=FetchType.LAZY,
	        optional=true) 
	@DescriptionsList
	Parieur parieur;
	@ManyToOne( 
	        fetch=FetchType.LAZY,
	        optional=true)
	@DescriptionsList
	evenement evenement;

}
